import os, json

SITE = "/home/claude/site"
CH_DIR = os.path.join(SITE, "challenges")

TRACKS = [
  dict(id="track-a", letter="A", name="AI & Emerging Technology Policy",
    tag="Tech / AI",
    card_desc="Produce a decision-ready governance package for a frontier-tech policy gap.",
    subtitle="Producing a decision-ready governance package for a frontier-tech policy gap",
    intro=["Frontier AI and emerging technologies are outpacing the policy infrastructure meant to govern them. This challenge asks teams to act as a rapid-response policy shop: take an unresolved emerging-tech governance question and produce a decision-ready package for a congressional office, federal agency, or think tank client."],
    tasks=["Select a governance gap (e.g., AI model evaluation standards, biosecurity screening for synthetic DNA, critical infrastructure cybersecurity, semiconductor export controls).",
           "Map the current regulatory/legislative landscape and identify the specific gap or conflict.",
           "Identify stakeholders (agencies, industry, civil society, international bodies) and their positions.",
           "Draft a policy option set with tradeoffs (not just one recommendation).",
           "Stress-test the proposal against a plausible adversarial or edge-case scenario."],
    approaches=["Legislative drafting — model bill language plus a section-by-section explainer.",
                "Regulatory — an agency rulemaking proposal (NIST, FTC, CISA-style) with cost-benefit analysis.",
                "Comparative — benchmark against EU AI Act, UK, or Japan frameworks.",
                "Red-team — build the proposal around a specific failure mode/incident scenario."],
    deliverables=["4–6 page policy memo (executive-summary style)","One-page issue brief / \u201cleave-behind\u201d",
                  "Slide deck (8–10 slides) for a 10-minute briefing","Annotated bibliography or source list",
                  "Process appendix (0.5 page)"],
    optional=["Model legislative or regulatory text (redlined)","Cost/fiscal impact or CBO-style scoring exercise",
              "Short (2–3 min) recorded elevator-pitch video","Public-comment-style submission to a real open rulemaking"],
    platforms=["Legislative tracking: Congress.gov, Regulations.gov, GovTrack","Comparative policy databases: OECD.AI Policy Observatory, EU AI Act tracker",
               "Drafting/collaboration: Google Docs, Notion, or a shared repo","Optional data/analysis: Python or R"],
    judging=[("Policy feasibility & political viability","25%"),("Technical accuracy","20%"),
             ("Clarity & persuasiveness of writing/briefing","20%"),("Stakeholder analysis depth","15%"),
             ("Originality of approach","10%"),("Handling of tradeoffs/edge cases","10%")],
    privacy=["Use only public, cite-able sources (statutes, agency filings, peer-reviewed research, reputable news).",
             "No non-public government data, leaked documents, or personal data on named private individuals.",
             "Disclose any AI-assisted drafting in an appendix.",
             "No fictionalized dialogue or misattributed quotes to real public officials."],
    team=["Teams of 3–5, interdisciplinary encouraged.","Suggested timeline: 3–4 weeks, plus 1 week for judging/briefing.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-b", letter="B", name="Health Policy Innovation",
    tag="Health",
    card_desc="Turn a real health-systems problem into a proposal that could move through a legislature or CMS.",
    subtitle="Translating a health-systems problem into a proposal that could realistically move through government",
    intro=["This challenge asks teams to translate a real health systems problem — access, cost, equity, or workforce — into a policy proposal that could realistically move through a state legislature, Congress, or a federal agency such as CMS."],
    tasks=["Choose a focus area: rural health access, behavioral health integration, aging/caregiving policy, maternal health, health data interoperability, or drug pricing.",
           "Ground the problem in data (prevalence, cost, disparities by geography/demographics).",
           "Review existing policy levers (state waivers, CMS rules, legislation, payer models).",
           "Design an intervention with an implementation pathway and funding mechanism.",
           "Identify equity impacts and unintended consequences."],
    approaches=["State-level pilot — propose a Medicaid waiver or state demonstration program.",
                "Federal rule/legislation — draft a CMS rule comment or bill concept with committee jurisdiction identified.",
                "Payment-model — design a value-based care or reimbursement structure.",
                "Community-based — center on a community health worker / social determinants intervention."],
    deliverables=["4–6 page policy brief with problem statement, evidence base, and recommendation",
                  "Implementation roadmap (who does what, in what sequence)","Budget/fiscal note",
                  "5-slide leadership briefing deck","Process appendix (0.5 page)"],
    optional=["Patient/provider journey map showing before/after the policy change",
              "Interview 1–2 practitioners or advocates (with consent)","Draft sample legislative or waiver language",
              "Equity impact assessment using a recognized framework"],
    platforms=["Data: CDC WONDER, KFF, CMS data.cms.gov, county health rankings",
               "Legislative tracking: Congress.gov, state legislature trackers, Regulations.gov",
               "Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Evidence quality & data use","25%"),("Feasibility (political + fiscal)","20%"),
             ("Equity analysis","20%"),("Clarity of implementation plan","20%"),("Presentation quality","15%")],
    privacy=["No individually identifiable patient data (PHI) — aggregate/public data only.",
             "Informed consent required for interviews; anonymize unless attribution is agreed.",
             "Treat any shared personal health information as sensitive by default.","Disclose AI tool use in an appendix."],
    team=["Teams of 3–5; a clinical/public-health background member is recommended.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-c", letter="C", name="Climate & Energy Policy",
    tag="Climate / Energy",
    card_desc="Design a decarbonization or resilience policy that balances environmental, economic, and equity goals.",
    subtitle="Balancing environmental, economic, and equity goals in a decarbonization or resilience policy",
    intro=["This challenge asks teams to design a decarbonization or climate-resilience policy that balances environmental, economic, and equity goals for a specific jurisdiction — city, state, or national."],
    tasks=["Select a focus: clean energy siting/permitting, grid reliability & AI data-center load, community-level decarbonization, climate finance/carbon markets, or climate adaptation/resilience.",
           "Establish the baseline (emissions, energy mix, or vulnerability data) for the chosen jurisdiction.",
           "Survey existing policy tools (incentives, mandates, carbon pricing, permitting reform).",
           "Propose a policy package with a phased implementation timeline.",
           "Model likely economic, environmental, and equity/community impacts."],
    approaches=["Permitting reform — streamlined siting rules with community-benefit safeguards.",
                "Market-based — a carbon pricing, cap-and-trade, or credit mechanism.",
                "Grid/tech — address AI-data-center load growth (rate design, interconnection reform).",
                "Community power — center a labor/union or frontline-community partnership model."],
    deliverables=["4–6 page policy brief with baseline data and a phased implementation plan",
                  "One-page fact sheet suitable for public/media release","Slide deck (8–10 slides)",
                  "Simple quantitative model or estimate of emissions/cost impact","Process appendix (0.5 page)"],
    optional=["Interactive chart/dashboard visualizing baseline vs. projected impact","Draft model legislative or regulatory text",
              "Mini stakeholder mapping exercise","Scenario-test against a supply shock or extreme weather event"],
    platforms=["Data: EIA, EPA GHG inventories, NREL data tools, state PUC filings",
               "Modeling: Excel/Sheets, Python (pandas), or simple emissions calculators",
               "Legislative tracking: Congress.gov, state legislature sites, Regulations.gov"],
    judging=[("Technical/scientific accuracy","20%"),("Political & economic feasibility","20%"),
             ("Equity/community impact analysis","20%"),("Quality of quantitative modeling","20%"),("Clarity & presentation","20%")],
    privacy=["Use only public emissions/energy data — no proprietary utility data without explicit permission.",
             "Consent and anonymization required for any community interviews.",
             "Disclose AI tool use and modeling assumptions/limitations transparently."],
    team=["Teams of 3–5, ideally with one member versed in energy/environmental data.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-d", letter="D", name="Economic & Fiscal Policy",
    tag="Economic / Fiscal",
    card_desc="Produce budget-scoring-quality analysis for a legislative or executive-branch client.",
    subtitle="Producing CBO/JCT-quality fiscal analysis for a live economic issue",
    intro=["This challenge asks teams to analyze a live fiscal or economic issue and produce budget-scoring-quality analysis for a legislative or executive-branch client — the kind of work CBO, JCT, or a state fiscal office would produce."],
    tasks=["Select a focus: tax policy reform, minimum wage/labor policy, housing affordability & zoning economics, trade/tariff impacts, public pension solvency, or small-business policy.",
           "Build a baseline using public economic data (BLS, BEA, Census, state revenue offices).",
           "Model at least two policy scenarios and their projected fiscal/economic effects.",
           "Identify distributional impacts (who gains, who pays, across income/region/demographic groups).",
           "Stress-test assumptions against a recession or high-inflation scenario."],
    approaches=["CBO-style scoring — a 10-year budgetary cost/revenue estimate with methodology notes.",
                "Distributional analysis — model impacts by income quintile, region, or industry.",
                "Comparative state — benchmark against states/countries that have tried the policy.",
                "Behavioral economics — incorporate likely behavioral responses into the model."],
    deliverables=["4–6 page policy brief with baseline data, model outputs, and recommendation",
                  "Fiscal/economic model (spreadsheet) with clearly labeled assumptions",
                  "One-page scorecard summarizing costs, revenues, distributional effects",
                  "Slide deck (8–10 slides)","Process appendix (0.5 page)"],
    optional=["Sensitivity analysis showing how results change under different assumptions",
              "Simple interactive calculator (e.g., \u201cestimate your household's impact\u201d)",
              "Comparative case study of a jurisdiction that implemented a similar policy",
              "A dissenting-view memo arguing the strongest opposing case"],
    platforms=["Data: BLS, BEA, Census Bureau, FRED, state revenue/budget offices, CBO/JCT public reports",
               "Modeling: Excel/Sheets, Python (pandas/numpy), R","Legislative tracking: Congress.gov, state fiscal notes"],
    judging=[("Rigor & transparency of modeling assumptions","25%"),("Data quality & sourcing","20%"),
             ("Distributional/equity analysis","20%"),("Political & administrative feasibility","20%"),("Clarity for non-economists","15%")],
    privacy=["Use only public, aggregate economic data — no proprietary firm-level or individual tax data.",
             "Disclose all modeling assumptions and data sources; no black-box models.",
             "Do not present modeled projections as certainties — communicate ranges."],
    team=["Teams of 3–5, at least one member comfortable with spreadsheet/statistical modeling.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-e", letter="E", name="Education Policy",
    tag="Education",
    card_desc="Design a policy response to a K-12 or higher-ed problem for a specific state or district.",
    subtitle="Designing a policy response to a K-12 or higher-education problem",
    intro=["This challenge asks teams to design a policy response to a K-12 or higher-education problem for a specific state or district context."],
    tasks=["Select a focus: learning loss/literacy recovery, teacher shortage & retention, school funding formulas, college access/affordability, early childhood education access, or chronic absenteeism.",
           "Ground the problem in state/district-level data (test scores, funding levels, demographic breakdowns).",
           "Review existing policy levers (state funding formulas, certification rules, financial aid programs).",
           "Design a policy proposal with an implementation and evaluation plan.",
           "Identify equity impacts across district wealth, race, and geography (urban/rural)."],
    approaches=["Funding formula — a revised state school-funding formula addressing an identified gap.",
                "Workforce — a teacher recruitment/retention policy (pay, loan forgiveness, certification pathways).",
                "Access — a higher-ed affordability or dual-enrollment expansion policy.",
                "Early intervention — center on early childhood or literacy-by-third-grade policy."],
    deliverables=["4–6 page policy brief with data, recommendation, and implementation plan",
                  "One-page fact sheet for a school board or state legislature audience","Slide deck (8–10 slides)",
                  "A simple evaluation plan (what metrics would show the policy is working)","Process appendix (0.5 page)"],
    optional=["Interview a teacher, administrator, or student (with consent)","Draft model state legislative or board-of-education rule language",
              "Simple data dashboard comparing districts/states","Cost-per-outcome analysis"],
    platforms=["Data: NCES, state department of education dashboards, EdBuild/school finance data, Census",
               "Legislative tracking: state legislature websites, Regulations.gov","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Evidence quality & data use","25%"),("Equity analysis (urban/rural, funding, demographic)","20%"),
             ("Feasibility (political + fiscal)","20%"),("Clarity of implementation & evaluation plan","20%"),("Presentation quality","15%")],
    privacy=["Use only public, aggregate education data — no individual student records (FERPA-protected data is off-limits).",
             "Guardian consent required for interviewing minors; anonymize identities.","Disclose AI tool use."],
    team=["Teams of 3–5; a current or former educator/administrator is a plus.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-f", letter="F", name="International Security & Foreign Policy",
    tag="Security / Foreign Policy",
    card_desc="Produce a foreign-policy or national-security memo for an NSC, State Dept, or committee audience.",
    subtitle="Producing a decision memo for a National Security Council or State Department audience",
    intro=["This challenge asks teams to produce a foreign-policy or national-security memo addressing a live geopolitical issue, written for a National Security Council, State Department, or congressional foreign-affairs-committee audience."],
    tasks=["Select a focus: great-power competition, alliance management, non-proliferation/arms control, sanctions policy, cybersecurity/critical infrastructure threats, or humanitarian/refugee policy.",
           "Assess the current state of play (recent developments, key actors, existing US posture).",
           "Identify US interests and constraints (legal, budgetary, alliance commitments).",
           "Draft a policy option set with a recommended course of action.",
           "War-game a plausible adversarial response to the recommended option."],
    approaches=["NSC memo — a decision memo format (options with pros/cons) for a senior decision-maker.",
                "Scenario/war-game — build the analysis around a specific crisis scenario.",
                "Alliance-coordination — focus on multilateral coordination (e.g., NATO or Five Eyes).",
                "Sanctions/economic statecraft — design a sanctions or export-control package and assess effectiveness."],
    deliverables=["4–6 page decision memo (options format)","One-page executive summary","Slide deck (8–10 slides)",
                  "A short risk register (top 3–5 risks of the recommended course)","Process appendix (0.5 page)"],
    optional=["Run a tabletop exercise/simulation with the team playing stakeholders","Draft talking points for a press briefing or testimony",
              "Open-source intelligence (OSINT) summary using only public reporting","A red-team memo arguing the adversary's likely strategy"],
    platforms=["Data/reporting: State Dept press briefings, DoD public statements, think tank trackers (CSIS, CNAS, Brookings, Belfer Center)",
               "Legislative tracking: Congress.gov","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Strategic soundness & feasibility","25%"),("Use of credible, current sourcing","20%"),
             ("Clarity of options and tradeoffs","20%"),("Anticipation of second-order/adversarial effects","20%"),("Presentation quality","15%")],
    privacy=["Open-source, publicly available information only — no classified, leaked, or non-public government material.",
             "Do not fabricate quotes or statements attributed to real officials.",
             "This challenge is strategic/policy analysis only, not operational planning.","Disclose AI tool use."],
    team=["Teams of 3–5, ideally with regional/language expertise represented.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-g", letter="G", name="Science & R&D Funding Policy",
    tag="Science / R&D Funding",
    card_desc="Redesign or defend a federal or state R&D funding mechanism.",
    subtitle="Redesigning how science gets funded, who decides, and how success is measured",
    intro=["This challenge asks teams to redesign or defend a federal or state R&D funding mechanism — how science gets funded, who decides, and how success is measured."],
    tasks=["Select a focus: NSF/NIH/DOE grant-making reform, indirect-cost-rate policy, basic-vs-applied research balance, research security/foreign-influence rules, or state-level R&D tax credits.",
           "Map the current funding architecture (agency, appropriations process, peer-review structure).",
           "Identify a specific inefficiency, gap, or political vulnerability in that architecture.",
           "Design a reform with an implementation and transition plan.",
           "Assess impact on research output, workforce pipeline, and national competitiveness."],
    approaches=["Appropriations — a funding reallocation proposal with fiscal notes.",
                "Process-reform — redesign peer review, grant timelines, or overhead-cost rules.",
                "Competitiveness — benchmark against China/EU/UK science-funding models.",
                "Pipeline — center on early-career researcher funding and retention."],
    deliverables=["4–6 page policy brief with baseline funding data and recommendation",
                  "One-page fact sheet for an appropriations subcommittee audience","Slide deck (8–10 slides)",
                  "A simple before/after funding-flow diagram","Process appendix (0.5 page)"],
    optional=["Interview a researcher or grants administrator (with consent)","Comparative case study of another country's science-funding model",
              "A researcher's-eye-view narrative of how the reform changes the grant-application experience","Draft model appropriations report language"],
    platforms=["Data: NSF NCSES, NIH RePORTER, DOE Office of Science budget documents, AAAS R&D budget tracker",
               "Legislative tracking: Congress.gov, agency budget justifications","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Understanding of the funding process","25%"),("Feasibility (political + administrative)","20%"),
             ("Impact on research quality/output","20%"),("Clarity of communication","20%"),("Originality","15%")],
    privacy=["Public budget documents and aggregate statistics only — no confidential reviewer deliberations or unpublished proposals.",
             "Consent and anonymization for any researcher interviews unless attribution is agreed.","Disclose AI tool use."],
    team=["Teams of 3–5; a member with research/academic-grant experience is a plus.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-h", letter="H", name="Workforce & Labor Policy",
    tag="Workforce / Labor",
    card_desc="Design a policy response to a live labor-market disruption for a specific industry or region.",
    subtitle="Responding to automation, skills gaps, or job-quality disruption in the labor market",
    intro=["This challenge asks teams to design a policy response to a live labor-market disruption — automation/AI displacement, skills gaps, or job-quality issues — for a specific industry or region."],
    tasks=["Select a focus: AI/automation workforce transition, apprenticeship & vocational training expansion, gig-economy worker classification, unemployment insurance modernization, or occupational licensing reform.",
           "Ground the problem in labor-market data (employment, wage, displacement trends).",
           "Review existing policy levers (UI, WIOA funding, licensing law, labor law).",
           "Design a policy proposal with an implementation and funding plan.",
           "Identify which workers/regions are most exposed and how the policy addresses that."],
    approaches=["Retraining — design or expand a reskilling/apprenticeship pipeline funded through workforce boards.",
                "Safety-net — modernize unemployment insurance or wage insurance for displaced workers.",
                "Regulatory — reform occupational licensing or gig-worker classification rules.",
                "Employer-incentive — design tax or subsidy incentives for job creation/retention."],
    deliverables=["4–6 page policy brief with labor-market data and recommendation",
                  "One-page fact sheet for a workforce board or state legislature audience","Slide deck (8–10 slides)",
                  "An implementation timeline showing funding sources and milestones","Process appendix (0.5 page)"],
    optional=["Interview a displaced worker, employer, or workforce-board staffer (with consent)",
              "Build a simple \u201cwho's exposed\u201d map by industry/region","Cost-per-job-saved or cost-per-worker-retrained analysis",
              "A dissenting-view memo from an employer or union perspective"],
    platforms=["Data: BLS, O*NET, state workforce agency dashboards, Census Bureau",
               "Legislative tracking: Congress.gov, state legislature sites","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Data-driven problem definition","25%"),("Feasibility (political + fiscal)","20%"),
             ("Equity across affected workers/regions","20%"),("Clarity of implementation plan","20%"),("Presentation quality","15%")],
    privacy=["Use only public, aggregate labor data — no individually identifiable worker records.",
             "Consent and anonymization for any worker interviews unless attribution is agreed.","Disclose AI tool use."],
    team=["Teams of 3–5; a member with HR, labor-economics, or workforce-board experience is a plus.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-i", letter="I", name="Environmental & Natural Resources Policy",
    tag="Environment / Conservation",
    card_desc="Address a non-carbon environmental problem: pollution, conservation, water quality, or justice.",
    subtitle="Addressing pollution, conservation, water quality, or environmental-justice problems",
    intro=["Distinct from the climate/decarbonization track, this challenge asks teams to address a non-carbon environmental problem: pollution, conservation, water quality, or environmental justice."],
    tasks=["Select a focus: PFAS/drinking-water contamination, air-quality permitting & environmental justice, public-lands/conservation management, plastics/waste policy, or biodiversity/endangered-species policy.",
           "Ground the problem in environmental monitoring data (EPA, USGS, state environmental agencies).",
           "Review existing regulatory tools (Clean Water Act, Clean Air Act, state permitting regimes).",
           "Design a policy proposal with an enforcement and monitoring mechanism.",
           "Identify which communities bear the greatest burden (environmental justice lens)."],
    approaches=["Regulatory — draft an EPA or state agency rule/permit-reform proposal.",
                "Community-remediation — center on a specific contaminated site or watershed.",
                "Market-based — design a conservation easement, cap-and-trade, or mitigation-banking mechanism.",
                "Environmental-justice — focus on cumulative-impact permitting for overburdened communities."],
    deliverables=["4–6 page policy brief with monitoring data and recommendation",
                  "One-page fact sheet for a public/community-meeting audience","Slide deck (8–10 slides)",
                  "A monitoring/enforcement plan showing how compliance would be tracked","Process appendix (0.5 page)"],
    optional=["Map affected communities against pollution-burden data (e.g., EPA EJScreen)","Interview a community member or local official (with consent)",
              "Draft model permit or rule language","Cost-benefit analysis of remediation vs. inaction"],
    platforms=["Data: EPA EJScreen, EPA ECHO, USGS, state environmental agency dashboards",
               "Legislative tracking: Regulations.gov, state legislature sites","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Scientific/technical accuracy","25%"),("Environmental justice analysis","20%"),
             ("Feasibility (regulatory + fiscal)","20%"),("Clarity of monitoring/enforcement plan","20%"),("Presentation quality","15%")],
    privacy=["Use only public environmental monitoring data — no proprietary industry data without permission.",
             "Consent and anonymization for any community interviews unless attribution is agreed.","Disclose AI tool use."],
    team=["Teams of 3–5; an environmental science or public-health background is a plus.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-j", letter="J", name="Energy & AI Data Center Infrastructure",
    tag="Energy / AI Data Centers",
    card_desc="Design a policy response to AI compute demand straining electric grids and ratepayer costs.",
    subtitle="Deciding how to permit, power, and pay for the AI data-center boom",
    intro=["AI compute demand is straining electric grids, driving up ratepayer costs, and forcing states to decide how to permit, power, and pay for data centers. This challenge asks teams to design a policy response for a specific grid region or state."],
    tasks=["Select a focus: data-center rate design, interconnection-queue reform, behind-the-meter/on-site generation permitting, water use for cooling, or transparency/siting disclosure requirements.",
           "Ground the problem in grid and load-growth data for the chosen region.",
           "Review existing regulatory tools (state PUC rate cases, FERC interconnection rules, local zoning/siting authority).",
           "Design a policy proposal balancing ratepayer protection, grid reliability, and continued investment.",
           "Assess tradeoffs: economic development benefits vs. reliability risk vs. cost-shifting to residential ratepayers."],
    approaches=["Rate-design — a special data-center rate class with minimum-take contracts to protect other ratepayers.",
                "Interconnection-reform — redesign the queue/process for large-load or generation interconnection.",
                "Siting/permitting — a state or local siting framework with community-benefit and disclosure requirements.",
                "Reliability — demand-response, curtailment, or on-site generation rules for data centers as flexible load."],
    deliverables=["4–6 page policy brief with load-growth/grid data and recommendation",
                  "One-page fact sheet for a state PUC or legislature audience","Slide deck (8–10 slides)",
                  "A simple cost-allocation table showing who pays under current rules vs. the reform","Process appendix (0.5 page)"],
    optional=["Build a simple load-growth projection chart for the chosen region","Interview a utility, PUC staffer, or community advocate (with consent)",
              "Comparative case study of another state's data-center rate case or siting rule","A ratepayer-impact one-pager in plain language"],
    platforms=["Data: EIA, FERC filings, state PUC dockets, grid operator (RTO/ISO) load forecasts",
               "Legislative tracking: state legislature sites, FERC eLibrary, Regulations.gov","Drafting/collaboration: Google Docs, shared repo"],
    judging=[("Technical grid/energy accuracy","25%"),("Ratepayer-protection analysis","20%"),
             ("Feasibility (regulatory + political)","20%"),("Balance of reliability, cost, and growth tradeoffs","20%"),("Presentation quality","15%")],
    privacy=["Use only public utility filings, PUC dockets, and EIA/FERC data — no proprietary data without permission.",
             "Do not include specific critical-infrastructure security vulnerabilities — keep analysis at the policy/rate-design level.","Disclose AI tool use."],
    team=["Teams of 3–5; an energy, utility-regulatory, or grid-engineering background is a plus.","Suggested timeline: 3–4 weeks.",
          "Final submission deadline: November 14, 2026."]),

  dict(id="track-l", letter="L", name="Open Track — Design Your Own Scope",
    tag="Open Track",
    card_desc="Scope your own policy problem, then move through the same analysis-and-briefing structure.",
    subtitle="Scoping your own policy problem before moving into full analysis and briefing",
    intro=["For teams who already have a policy issue they care about that doesn't fit neatly into the other tracks, or who want the challenge of scoping their own problem the way a real fellow does in the first weeks of a placement. The team's first deliverable is the scope itself — defined, justified, and bounded — before moving into the same analysis-and-briefing structure as the other tracks."],
    tasks=["Identify a policy problem in any domain — can combine or cut across the other tracks.",
           "Write a one-paragraph problem statement and justify why it matters and why now.",
           "Define scope boundaries explicitly: jurisdiction, timeframe, and population/stakeholders affected. State what's out of scope and why.",
           "Get scope approved by an instructor/judge/mentor before proceeding.",
           "Proceed through the same core policy tasks as any track: landscape/stakeholder mapping, options analysis, recommendation, tradeoffs."],
    approaches=["Cross-track fusion — deliberately combine two tracks' subject areas into one proposal.",
                "Hyper-local — scope down to a single city, campus, or agency rather than state/national level.",
                "Personal-experience — start from a problem the team has direct experience with.",
                "Frontier-issue — pick something genuinely unsettled that doesn't have an established policy playbook yet."],
    deliverables=["Scope memo (1 page): problem statement, jurisdiction, timeframe, stakeholders, explicit out-of-scope boundaries — submitted and approved before full work begins",
                  "4–6 page policy brief (same standard as other tracks)","One-page fact sheet / leave-behind","Slide deck (8–10 slides)"],
    optional=["Same menu as other tracks (model legislative text, interactive dashboard, interviews, dissenting-view memo, etc.) — team selects what fits",
              "A short reflection on why they scoped the problem the way they did and what they deliberately excluded"],
    platforms=["Same general categories as other tracks — team selects tools appropriate to their chosen domain.",
               "Teams are encouraged to identify their own authoritative data source(s) as part of the scoping step."],
    judging=[("Quality and defensibility of the scope itself","20%"),("Policy feasibility & rigor","25%"),
             ("Clarity & persuasiveness of writing/briefing","20%"),("Stakeholder analysis depth","15%"),
             ("Originality of problem selection","10%"),("Handling of tradeoffs/edge cases","10%")],
    privacy=["Same baseline rules as all other tracks: public/cite-able sources only, no non-public government or proprietary data.",
             "Informed consent and anonymization for any interviews; AI tool use disclosed in an appendix.",
             "Team is responsible for flagging domain-specific data-sensitivity issues (health data, minors, national security) in the scope memo."],
    team=["Teams of 3–5.","Scope memo due early (e.g., end of week 1) with a go/no-go check from organizers before further work.",
          "Suggested overall timeline: 3–4 weeks. Final submission deadline: November 14, 2026."]),
]

NAV = """<header class="site">
  <nav class="bar">
    <a class="logo" href="{root}index.html">
      <span class="logo-mark">SNAP</span>
      <span class="logo-sub">Scientist Network for Advancing Policy</span>
    </a>
    <ul class="nav-links">
      <li><a href="{root}index.html#challenges">All Challenges</a></li>
      <li><a href="{root}index.html#how-it-works">How It Works</a></li>
    </ul>
  </nav>
</header>"""

FOOTER = """<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4 style="font-size:1rem;">Scientist Network for Advancing Policy (SNAP)</h4>
        <p>Advancing applied policy research from the classroom to the field.</p>
      </div>
      <div>
        <a href="{root}index.html#challenges">All Challenges</a>
        <a href="{root}index.html#how-it-works">How It Works</a>
      </div>
      <div>
        <a href="mailto:hello@example.com">Contact</a>
      </div>
    </div>
    <span>&copy; 2026 Scientist Network for Advancing Policy (SNAP).</span>
  </div>
</footer>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body>
"""

def li(items):
    return "\n".join(f"        <li>{x}</li>" for x in items)

def oli(items):
    return "\n".join(f"        <li>{x}</li>" for x in items)

def judging_rows(pairs):
    return "\n".join(f'        <tr><td>{c}</td><td>{w}</td></tr>' for c, w in pairs)

def build_track_page(t):
    root = "../"
    title = f"Track {t['letter']} — {t['name']} | SNAP"
    doc = f"https://docs.google.com/document/d/REPLACE_WITH_DOC_ID_{t['id']}/edit"
    discord = f"https://discord.gg/REPLACE_WITH_INVITE_{t['id']}"
    form = "https://docs.google.com/forms/d/e/REPLACE_WITH_FORM_ID/viewform"

    html = HEAD.format(title=title, root=root)
    html += NAV.format(root=root) + "\n"
    html += '<div class="wrap layout">\n  <main class="content">\n'
    html += f'    <a class="backlink" href="{root}index.html#challenges">&larr; All challenges</a>\n'
    html += f'    <span class="eyebrow">Policy Hackathon &middot; Track {t["letter"]}</span>\n'
    html += f'    <h1 class="title">{t["name"]}</h1>\n'
    html += f'    <h2 class="subtitle">{t["subtitle"]}</h2>\n'
    html += '    <div class="intro">\n'
    for p in t["intro"]:
        html += f'      <p>{p}</p>\n'
    html += '    </div>\n'

    html += '    <div class="cta-row">\n'
    html += f'      <a class="btn btn-secondary" href="{doc}" target="_blank" rel="noopener">Challenge Document</a>\n'
    html += f'      <a class="btn btn-ghost" href="{discord}" target="_blank" rel="noopener">Join the Track {t["letter"]} Discord</a>\n'
    html += f'      <a class="btn btn-primary" href="{form}" target="_blank" rel="noopener">Submit Your Project</a>\n'
    html += '    </div>\n'

    html += f'''    <section class="block">
      <h2>Key Project Tasks</h2>
      <ol>
{oli(t["tasks"])}
      </ol>
    </section>

    <section class="block">
      <h2>Possible Approaches</h2>
      <ol>
{oli(t["approaches"])}
      </ol>
    </section>

    <div class="two-col">
      <section class="block" style="border-top:none;">
        <h2>Required Deliverables</h2>
        <ul>
{li(t["deliverables"])}
        </ul>
      </section>
      <section class="block" style="border-top:none;">
        <h2>Optional Advanced Tasks</h2>
        <ul>
{li(t["optional"])}
        </ul>
      </section>
    </div>

    <section class="block">
      <h2>Platforms &amp; Tools</h2>
      <ul>
{li(t["platforms"])}
      </ul>
    </section>

    <section class="block">
      <h2>Judging Criteria</h2>
      <table class="judging">
        <tr><th>Criterion</th><th>Weight</th></tr>
{judging_rows(t["judging"])}
      </table>
    </section>

    <section class="block">
      <h2>Data &amp; Privacy Requirements</h2>
      <ul>
{li(t["privacy"])}
      </ul>
    </section>

    <section class="block">
      <h2>Team &amp; Deadline</h2>
      <ul>
{li(t["team"])}
      </ul>
    </section>

    <div class="signup">
      <div>
        <h3>Stay in the loop</h3>
        <p>Get track updates and deadline reminders by email.</p>
      </div>
      <form class="email-form" action="https://formspree.io/f/REPLACE_WITH_FORM_ID" method="POST">
        <input type="email" name="email" placeholder="you@example.com" required>
        <button type="submit">Subscribe</button>
      </form>
    </div>

  </main>

  <aside class="promo">
    <h4>Join the Network</h4>
    <p>Looking for policy researchers and analysts for future programs.</p>
    <a class="btn-small" href="https://example.com/apply" target="_blank" rel="noopener">Apply Now</a>
  </aside>
</div>
'''
    html += FOOTER.format(root=root)
    html += "\n</body>\n</html>\n"
    return html

def build_index():
    root = ""
    cards = ""
    for t in TRACKS:
        cards += f'''      <article class="card">
        <span class="tag">Track {t['letter']} &middot; {t['tag']}</span>
        <h3>{t['name']}</h3>
        <p>{t['card_desc']}</p>
        <a class="learn" href="challenges/{t['id']}.html">View challenge &rarr;</a>
      </article>
'''
    html = HEAD.format(title="Policy Hackathon — Industry Challenge Tracks | SNAP", root=root)
    html += NAV.format(root=root) + "\n"
    html += '''<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Submission deadline &middot; November 14, 2026</span>
    <h1>Policy Hackathon: Industry Challenge Tracks</h1>
    <p class="lede">Teams work through one of eleven challenge tracks, applying policy analysis,
      research, and briefing skills to a live governance problem.</p>
    <div class="cta-row">
      <a class="btn btn-secondary" href="https://docs.google.com/document/d/REPLACE_WITH_ORIENTATION_DOC_ID/edit" target="_blank" rel="noopener">Orientation Guide</a>
      <a class="btn btn-primary" href="https://docs.google.com/forms/d/e/REPLACE_WITH_FORM_ID/viewform" target="_blank" rel="noopener">Submit Your Project</a>
      <a class="btn btn-ghost" href="https://discord.gg/REPLACE_WITH_INVITE" target="_blank" rel="noopener">Join the Community Discord</a>
    </div>
  </div>
</section>

<section class="section" id="challenges">
  <div class="wrap">
    <div class="section-head">
      <h2>Choose a Track</h2>
      <p>Each card links to the full challenge page with tasks, deliverables, judging criteria, and submission links.</p>
    </div>
    <div class="grid">
''' + cards + '''    </div>
  </div>
</section>

<section class="section" id="how-it-works">
  <div class="wrap">
    <div class="section-head"><h2>How It Works</h2></div>
    <div class="steps">
      <div class="step"><span class="step-num">01</span><div class="step-body"><h4>Register</h4><p>Sign up for the free challenge track.</p></div></div>
      <div class="step"><span class="step-num">02</span><div class="step-body"><h4>Pick a track</h4><p>Review the eleven tracks and choose the one that fits your team.</p></div></div>
      <div class="step"><span class="step-num">03</span><div class="step-body"><h4>Form a team</h4><p>Teams of 3&ndash;5, interdisciplinary encouraged.</p></div></div>
      <div class="step"><span class="step-num">04</span><div class="step-body"><h4>Submit by August 7</h4><p>One teammate submits final materials through the official form.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="signup">
      <div>
        <h3>Stay in the loop</h3>
        <p>Get challenge updates and deadline reminders by email.</p>
      </div>
      <form class="email-form" action="https://formspree.io/f/REPLACE_WITH_FORM_ID" method="POST">
        <input type="email" name="email" placeholder="you@example.com" required>
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </div>
</section>
'''
    html += FOOTER.format(root=root)
    html += "\n</body>\n</html>\n"
    return html

os.makedirs(CH_DIR, exist_ok=True)
with open(os.path.join(SITE, "index.html"), "w") as f:
    f.write(build_index())

for t in TRACKS:
    with open(os.path.join(CH_DIR, f"{t['id']}.html"), "w") as f:
        f.write(build_track_page(t))

print("Built index.html +", len(TRACKS), "track pages")
