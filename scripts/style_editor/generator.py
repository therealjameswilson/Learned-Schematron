    from .rules_model import StyleConfig

    def generate_schematron(cfg: StyleConfig) -> str:
        # Render a Schematron that covers date/@when preference, note/@type set,
        # and Source: note heuristics based on cfg.
        allowed_types = " ".join(cfg.allowed_note_types) if cfg.allowed_note_types else "source editorial textual crossreference"
        sch = f"""<schema xmlns="http://purl.oclc.org/dsdl/schematron"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  xmlns:sqf="http://www.schematron-quickfix.com/validator/process"
  queryBinding="xslt2">
  <title>FRUS Style Guide Editor — Exported Rules</title>

  <pattern id="date-when">
    <rule context="tei:div[@type='document']/tei:opener/tei:dateline/tei:date">
      <assert test="@when" sqf:fix="addWhen">Dateline <date> must have @when.</assert>
      <assert test="matches(@when,'^\\d{{4}}(-\\d{{2}}(-\\d{{2}})?)?$')" sqf:fix="shapeWhen">Use ISO @when.</assert>
      <sqf:fix id="addWhen"><sqf:add match="." node-type="attribute" target="when">{'YYYY-MM-DD' if cfg.prefer_when=='YYYY-MM-DD' else cfg.prefer_when}</sqf:add></sqf:fix>
      <sqf:fix id="shapeWhen"><sqf:add match="." node-type="attribute" target="when">{'YYYY-MM-DD' if cfg.prefer_when=='YYYY-MM-DD' else cfg.prefer_when}</sqf:add></sqf:fix>
    </rule>
  </pattern>

  <pattern id="note-type">
    <rule context="tei:note">
      <assert test="@type" sqf:fix="setType">note/@type is required.</assert>
      <assert test="@type and contains('{allowed_types}', @type)">note/@type should be one of: {allowed_types}.</assert>
      <sqf:fix id="setType"><sqf:add match="." node-type="attribute" target="type">{cfg.allowed_note_types[0] if cfg.allowed_note_types else 'editorial'}</sqf:add></sqf:fix>
    </rule>
  </pattern>

  <pattern id="source-notes">
    <rule context="tei:note[matches(normalize-space(string(.)), '^Source:', 'i')]">
      {"<assert test="matches(normalize-space(string(.)), '\\.$')" sqf:fix="endPeriod">Source note should end with a period.</assert>" if cfg.source_simple_fixes.get('terminal_period', True) else ""}
      {"<report test="not(contains(string(.), ';'))" sqf:fix="insertSemicolons">Source notes typically separate elements with semicolons.</report>" if cfg.source_simple_fixes.get('prefer_semicolons', True) else ""}

      <!-- Heuristic repo shapes (if provided) -->
      {"<report test="matches(string(.), 'Presidential\\s+Library') and not(matches(string(.), '"+cfg.source_patterns.get('presidential_library','')+"'))" sqf:fix="libShape">Presidential Library pattern differs from configured expectation.</report>" if cfg.source_patterns.get('presidential_library') else ""}
      {"<report test="matches(string(.), '\\b(National Archives|NARA)\\b') and not(matches(string(.), '"+cfg.source_patterns.get('nara_rg','')+"'))" sqf:fix="naraShape">NARA pattern differs from configured expectation.</report>" if cfg.source_patterns.get('nara_rg') else ""}
      {"<report test="matches(string(.), 'Department of State') and not(matches(string(.), '"+cfg.source_patterns.get('state_dept','')+"'))" sqf:fix="dosShape">Department of State pattern differs from configured expectation.</report>" if cfg.source_patterns.get('state_dept') else ""}
      {"<report test="matches(string(.), '\\b(Central Intelligence Agency|CIA)\\b') and not(matches(string(.), '"+cfg.source_patterns.get('cia','')+"'))" sqf:fix="ciaShape">CIA pattern differs from configured expectation.</report>" if cfg.source_patterns.get('cia') else ""}

      <sqf:fix id="endPeriod">
        <sqf:description><sqf:title>Add terminal period</sqf:title></sqf:description>
        <sqf:replace match="text()"><value-of select="concat(normalize-space(.), '.')"/></sqf:replace>
      </sqf:fix>
      <sqf:fix id="insertSemicolons">
        <sqf:description><sqf:title>Suggest inserting semicolons</sqf:title></sqf:description>
      </sqf:fix>
      <sqf:fix id="libShape"><sqf:description><sqf:title>Adjust to Presidential Library pattern</sqf:title></sqf:description></sqf:fix>
      <sqf:fix id="naraShape"><sqf:description><sqf:title>Adjust to NARA pattern</sqf:title></sqf:description></sqf:fix>
      <sqf:fix id="dosShape"><sqf:description><sqf:title>Adjust to Department of State pattern</sqf:title></sqf:description></sqf:fix>
      <sqf:fix id="ciaShape"><sqf:description><sqf:title>Adjust to CIA pattern</sqf:title></sqf:description></sqf:fix>
    </rule>
  </pattern>
</schema>
"""
        return sch
