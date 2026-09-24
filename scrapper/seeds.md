List of Sources
One seed per domain by default -- crawl.py deep-crawls each seed to MAX_DEPTH/MAX_PAGES_PER_DOMAIN, so a single well-chosen entry point usually reaches a domain's industry/case-study pages organically. Exception -- a firm's people/leadership bio section is often a disconnected content tree not reachable from its industries/services hub within budget (confirmed on EY, where seeding only /industries produced 173 pages but just 2 candidate_profile hits) -- those firms get an explicit second seed in "People / Leadership Hubs" below. crawl.py's dedup is per-seed-URL, not per-domain, so two seeds on the same domain both run.
M&A & Financial Advisory
EY: https://www.ey.com/en_gl/industries
PWC: https://www.pwc.com/sg/en/services/consulting.html
Deloitte: https://www.deloitte.com/us/en/services/consulting/services/mergers-acquisitions.html
KPMG: https://kpmg.com/xx/en/what-we-do/services/advisory/deal-advisory/our-capabilities/transaction-services.html
McKinsey: https://www.mckinsey.com/capabilities/m-and-a/how-we-help-clients
BCG: https://www.bcg.com/capabilities/mergers-acquisitions-transactions-pmi/due-diligence
Bain: https://www.bain.com/industry-expertise/private-equity/due-diligence/
Accenture: https://www.accenture.com/us-en/services/technology-transformation
Alvarez & Marsal: https://www.alvarezandmarsal.com/expertise
FTI Consulting: https://www.fticonsulting.com/services
Grant Thornton: https://www.grantthornton.com/
BDO: https://www.bdo.com/
RSM: https://rsmus.com/
Kroll (Duff & Phelps): https://www.kroll.com/en
(McKinsey has returned 0 pages on every seed tried so far, bot-blocked -- kept in case that changes, not expected to yield much)
Industrial, Energy & Built Environment
AESG: https://aesg.com/sg/
ERM: https://www.erm.com/
WSP: https://www.wsp.com/
Arup: https://www.arup.com/
DNV: https://www.dnv.com/
Technology, Product & Data
IBM Consulting: https://www.ibm.com/consulting
Publicis Sapient: https://www.publicissapient.com/
ThoughtWorks: https://www.thoughtworks.com/
Slalom: https://www.slalom.com/
West Monroe: https://www.westmonroe.com/
Capgemini Invent: https://www.capgemini.com/service/capgemini-invent/
Legal
Axiom: https://www.axiomlaw.com/
Elevate Services: https://www.elevateservices.com/
UnitedLex: https://unitedlex.com/
Boutique Strategy & M&A Advisory
Oliver Wyman: https://www.oliverwyman.com/
Roland Berger: https://www.rolandberger.com/en/
L.E.K. Consulting: https://www.lek.com/
Kearney: https://www.kearney.com/
Strategy& (PwC): https://www.strategyand.pwc.com/
Teneo: https://www.teneo.com/
Ankura: https://ankura.com/
Berkeley Research Group: https://www.thinkbrg.com/
Charles River Associates: https://www.crai.com/
Houlihan Lokey: https://hl.com/
Lazard: https://www.lazard.com/
Evercore: https://www.evercore.com/
Moelis & Company: https://www.moelis.com/
Rothschild & Co: https://www.rothschildandco.com/
Existing White Collar gig site
Upwork: https://www.upwork.com
Fiverr Pro: https://www.fiverr.com/pro
Braintrust: https://www.usebraintrust.com/
A.Team: https://www.a.team/
Gig / Consultancy Case Study Hubs
Consultport: https://consultport.com/case-studies/
Toptal: https://www.toptal.com/clients
Catalant: https://catalant.com/for-independent-consultants/
Business Talent Group: https://businesstalentgroup.com/category/case-studies/
MBO Partners: https://www.mbopartners.com/case-studies/
GLG (Gerson Lehrman Group): https://glginsights.com/case-studies
Expert360: https://expert360.com/
Graphite: https://graphite.com/
Paro: https://paro.ai/
AlphaSights: https://www.alphasights.com/
Guidepoint: https://www.guidepoint.com/
Third Bridge: https://www.thirdbridge.com/
Coleman Research: https://www.colemanrp.com/
Executive Search & Interim Leadership
Heidrick & Struggles: https://www.heidrick.com/
Spencer Stuart: https://www.spencerstuart.com/
Korn Ferry: https://www.kornferry.com/
Russell Reynolds Associates: https://www.russellreynolds.com/
Egon Zehnder: https://www.egonzehnder.com/
DHR Global: https://www.dhrglobal.com/
Interim Partners: https://www.interimpartners.com/
Eden McCallum: https://www.edenmccallum.com/
RGP (Resources Global Professionals): https://rgp.com/
The CFO Centre: https://www.thecfocentre.com/
Chief Outsiders: https://www.chiefoutsiders.com/
Insurance, Wealth & Asset Management
Willis Towers Watson: https://www.wtwco.com/
Mercer: https://www.mercer.com/
Marsh McLennan: https://www.marsh.com/
Milliman: https://www.milliman.com/
Real Estate & Built Environment
JLL: https://www.jll.com/
CBRE: https://www.cbre.com/
Cushman & Wakefield: https://www.cushmanwakefield.com/
Savills: https://www.savills.com/
AECOM: https://aecom.com/
Jacobs: https://www.jacobs.com/
Telecom, Media & Aerospace Advisory
Analysys Mason: https://www.analysysmason.com/
STL Partners: https://stlpartners.com/
ICF International: https://www.icf.com/
People / Leadership Hubs (second seed, same domain as above -- see note at top of file)
EY (People): https://www.ey.com/en_gl/people
Bain (People): https://www.bain.com/our-team/
PwC (Leadership): https://www.pwc.com/gx/en/about/leadership.html
(BCG/KPMG/Deloitte/Accenture people hubs not yet found -- every guessed URL either 404'd or landed on the wrong page, e.g. Deloitte's /about/people.html is actually a "Life at Deloitte" careers page, not bios. Confirmed real individual profile URLs exist on all four -- e.g. bcg.com/about/people/experts/<name>, kpmg.com/us/en/how-we-work/people/<letter>/<name>.html -- but the index/hub page hasn't been located. Next attempt is to seed directly from one confirmed individual profile URL per firm instead of guessing a hub, and see if the crawler finds a "similar experts" or "meet the team" link from there.)

Coverage Expansion -- added 20 Sep 2026
The 86 seeds above are all professional-services firms, so the corpus is dominated by a few consulting domains. These seeds reach beyond them. Each was picked for having BOTH named individual bios and concrete project case studies, which is what classify.py's PROVIDER and HIRER labels need. Every URL below returned 200 to a plain GET on 20 Sep 2026.
Science and Engineering Consulting
Exponent: https://www.exponent.com/
Cambridge Consultants: https://www.cambridgeconsultants.com/
Southwest Research Institute: https://www.swri.org/
Element Materials Technology: https://www.element.com/
Life Sciences and Health
IQVIA: https://www.iqvia.com/
Parexel: https://www.parexel.com/
Avalere Health: https://avalere.com/
ClearView Healthcare Partners: https://www.clearviewhcp.com/
Trinity Life Sciences: https://www.trinitylifesciences.com/
Environment, Land and Landscape
Ramboll: https://www.ramboll.com/
Arcadis: https://www.arcadis.com/
RSK Group: https://www.rskgroup.com/
SWA Group: https://www.swagroup.com/
OLIN: https://theolinstudio.com/
Architecture Practices
Gensler: https://www.gensler.com/
Perkins and Will: https://www.perkinswill.com/
Design, Brand and Creative
Pentagram: https://www.pentagram.com/
IDEO: https://www.ideo.com/
Wolff Olins: https://www.wolffolins.com/
Landor: https://www.landor.com/
Sound and Music Branding
Made in Music: https://www.madeinmusic.com/
Sixieme Son: https://www.sixiemeson.com/
Performance and Communication Training
RADA Business: https://www.radabusiness.com/
Language and Localization
RWS: https://www.rws.com/
Lionbridge: https://www.lionbridge.com/
Welocalize: https://www.welocalize.com/
Acclaro: https://www.acclaro.com/
Publishing and Editorial
Reedsy: https://www.reedsy.com/
Heritage and Archaeology
MOLA Museum of London Archaeology: https://www.mola.org.uk/
Wessex Archaeology: https://www.wessexarch.co.uk/
Oxford Archaeology: https://oxfordarchaeology.com/
Ralph Appelbaum Associates: https://www.raa.com/
Ethnography and Social Research
ReD Associates: https://www.redassociates.com/
Stripe Partners: https://www.stripepartners.com/
Business Ethics
Ethisphere: https://www.ethisphere.com/
Blocked on a plain GET, worth retrying through crawl4ai's real browser
These returned 403 to curl, which is usually plain-UA bot detection rather than a dead site, so they are held here rather than discarded. Try them with crawl4ai before writing them off. Thornton Tomasetti, Simpson Gumpertz and Heger, Battelle, Certara, NAMSA, RQM+, HOK, Sasaki, Tetra Tech, Stantec, Health Advances, Putnam Associates, The Ethics Centre.
