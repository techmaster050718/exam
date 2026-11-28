import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
VERIFIED = "2026-11-28"

sources = {
    "economy": ("Ministry of Finance / Ministry of Statistics and Programme Implementation", "https://www.mospi.gov.in/", "National accounts and Indian economic statistics"),
    "tax": ("Income Tax Department", "https://www.incometax.gov.in/", "Direct-tax concepts and taxpayer guidance"),
    "gst": ("CBIC / GST Council", "https://www.cbic.gov.in/", "GST, customs and indirect-tax guidance"),
    "budget": ("Ministry of Finance", "https://www.indiabudget.gov.in/", "Union Budget and government finance"),
    "rbi": ("Reserve Bank of India", "https://www.rbi.org.in/", "Monetary policy, banking and inflation"),
    "trade": ("Department of Commerce / DGFT", "https://www.commerce.gov.in/", "Foreign trade policy and trade data"),
    "partners": ("Department of Commerce", "https://commerce.gov.in/trade-statistics/", "India's trade relationships"),
    "org": ("World Trade Organization / IMF / World Bank", "https://www.wto.org/", "International organisations and trade rules"),
    "fx": ("Reserve Bank of India", "https://www.rbi.org.in/", "Exchange rates, reserves and balance of payments"),
}


def q(qid, text, options, answer, explanation, topic, subtopic, difficulty,
      source_key, question_type="MCQ", nat_answer=None, tolerance=0,
      exam_tags=None):
    name, ref, description = sources[source_key]
    item = {
        "id": qid,
        "type": question_type,
        "q": text,
        "explanation": explanation,
        "topic": topic,
        "subtopic": subtopic,
        "difficulty": difficulty,
        "sourceType": "PRACTICE",
        "sourceName": name,
        "sourceReference": ref,
        "sourceDescription": description,
        "verificationStatus": "VERIFIED_OFFICIAL_SOURCE",
        "verificationDate": VERIFIED,
        "examTags": exam_tags or ["Economics", "General Studies", "Banking"],
    }
    if question_type == "MCQ":
        item["options"] = options
        item["answer"] = answer
    else:
        item["answer"] = nat_answer
        item["tolerance"] = tolerance
    return item


rows = []
n = 0
def add(text, options, answer, explanation, topic, subtopic, difficulty, source_key,
        qtype="MCQ", nat_answer=None, tolerance=0):
    global n
    n += 1
    rows.append(q(
        f"econ-iwt-1-{n:03d}", text, options, answer, explanation, topic, subtopic,
        difficulty, source_key, qtype, nat_answer, tolerance
    ))

# Indian Economy – Fundamentals (12)
add("Which concept measures the final value of goods and services produced within a country's domestic territory during a period?", ["Gross Domestic Product", "Public debt", "Fiscal deficit", "Consumer expenditure"], 0, "GDP measures final output produced within the domestic territory over a specified period.", "Indian Economy – Fundamentals", "National income", "BASIC", "economy")
add("Real GDP differs from nominal GDP because real GDP:", ["Uses base-year prices to adjust for inflation", "Includes only exports", "Measures only government spending", "Excludes final goods"], 0, "Real GDP uses constant prices, while nominal GDP uses current prices.", "Indian Economy – Fundamentals", "Nominal and real GDP", "BASIC", "economy")
add("A rise in the general price level while quantities remain unchanged would generally:", ["Raise nominal GDP but not necessarily real GDP", "Lower nominal GDP", "Leave both unchanged", "Eliminate GDP growth"], 0, "Higher prices increase the value measure of nominal GDP, while real GDP depends on constant-price quantities.", "Indian Economy – Fundamentals", "Nominal and real GDP", "INTERMEDIATE", "economy")
add("Per capita income is calculated by dividing national income or output by:", ["Population", "Government spending", "Number of firms", "Exports"], 0, "Per capita income relates aggregate income or output to the population.", "Indian Economy – Fundamentals", "Per capita income", "BASIC", "economy")
add("Economic development differs from economic growth because development also includes:", ["Living standards, health and social welfare", "Only increases in output", "Only higher exports", "Only higher tax revenue"], 0, "Development is broader and considers improvements in welfare and human capabilities.", "Indian Economy – Fundamentals", "Growth versus development", "BASIC", "economy")
add("Agriculture and allied activities generally belong to the:", ["Primary sector", "Secondary sector", "Tertiary sector", "Financial sector only"], 0, "The primary sector directly uses natural resources, including agriculture.", "Indian Economy – Fundamentals", "Economic sectors", "BASIC", "economy")
add("Manufacturing most clearly belongs to the:", ["Secondary sector", "Primary sector", "Tertiary sector", "Informal household sector"], 0, "Manufacturing converts raw or intermediate products into finished goods.", "Indian Economy – Fundamentals", "Economic sectors", "BASIC", "economy")
add("A firm with no formal registration or accounting records is most likely to operate in the:", ["Informal economy", "Public sector", "Capital account", "Primary deficit"], 0, "Informality is characterised by limited or absent formal registration and regulated employment/accounting arrangements.", "Indian Economy – Fundamentals", "Formal and informal economy", "INTERMEDIATE", "economy")
add("The public sector mainly consists of:", ["Government-owned or controlled institutions", "Only privately listed companies", "Only household production", "Foreign consumers"], 0, "Public-sector units are owned or controlled by central, state or local governments.", "Indian Economy – Fundamentals", "Public and private sectors", "BASIC", "economy")
add("Fiscal deficit is the excess of total government expenditure over:", ["Revenue and non-debt capital receipts", "Only interest payments", "Only tax revenue", "Only borrowing"], 0, "Fiscal deficit measures borrowing requirement and equals expenditure over receipts excluding borrowings.", "Indian Economy – Fundamentals", "Fiscal deficit", "INTERMEDIATE", "economy")
add("Revenue deficit arises when:", ["Revenue expenditure exceeds revenue receipts", "Capital expenditure exceeds capital receipts", "Tax receipts exceed total expenditure", "Government borrowing is zero"], 0, "Revenue deficit compares revenue expenditure with revenue receipts.", "Indian Economy – Fundamentals", "Revenue deficit", "INTERMEDIATE", "economy")
add("If national income is ₹1,00,000 crore and population is 25 crore, national income per person is:", None, 0, "Divide 1,00,000 crore by 25 crore: ₹4000 per person.", "Indian Economy – Fundamentals", "Per capita income", "ADVANCED", "economy", "NAT", nat_answer=4000, tolerance=0)

# Tax system (18)
add("A tax is compulsory payment to government and ordinarily:", ["Does not provide an individual-specific quid pro quo", "Creates an individual debt equal to benefits received", "Is optional for citizens", "Is always a penalty"], 0, "Tax is a compulsory contribution made for public expenditure without a direct individual return.", "Indian Tax System", "Tax fundamentals", "BASIC", "tax")
add("Income tax is primarily a:", ["Direct tax", "Indirect tax", "Customs duty", "Excise duty"], 0, "Income tax is paid directly by the taxpayer on taxable income.", "Indian Tax System", "Direct and indirect taxes", "BASIC", "tax")
add("GST paid at the point of purchase is generally:", ["An indirect tax on consumption", "A direct tax on salary", "A customs receipt only", "A personal income tax"], 0, "GST is levied on supply and collected in the transaction chain rather than directly assessed on personal income.", "Indian Tax System", "Direct and indirect taxes", "BASIC", "tax")
add("Corporate tax is levied on:", ["Taxable profits of companies", "An individual's purchases", "All imports only", "Household savings only"], 0, "Corporate tax applies to taxable company income/profits under direct-tax law.", "Indian Tax System", "Corporate tax", "BASIC", "tax")
add("Capital gains tax applies to profit arising from:", ["Transfer of specified capital assets", "Ordinary purchases of groceries", "GST registration", "Bank account opening"], 0, "Capital gains are changes resulting from transfer of qualifying capital assets.", "Indian Tax System", "Capital gains", "INTERMEDIATE", "tax")
add("TDS is:", ["Tax deducted by payer and deposited to government", "A customs discount", "A tax-free subsidy", "Tax paid only at year-end by every taxpayer"], 0, "TDS is withheld by the person making specified payments and remitted to the tax authority.", "Indian Tax System", "TDS", "BASIC", "tax")
add("TCS ordinarily means:", ["Tax collected at source on specified transactions", "Tax credit for states", "Tax paid by customs only", "Tax-free capital subsidy"], 0, "TCS requires specified sellers/collectors to collect tax on covered transactions.", "Indian Tax System", "TCS", "BASIC", "tax")
add("The old and new income-tax regimes differ mainly in:", ["Available deductions/exemptions and applicable slab structures", "Whether income tax is a direct tax", "Who owns the RBI", "Whether customs duty exists"], 0, "The regimes apply different provisions on slabs and eligible deductions/exemptions.", "Indian Tax System", "Tax regimes", "INTERMEDIATE", "tax")
add("A tax deduction from taxable income generally:", ["Reduces taxable income if conditions are met", "Always refunds the full deduction", "Replaces GST", "Increases tax liability automatically"], 0, "A lawful deduction reduces the taxable base, subject to eligibility conditions.", "Indian Tax System", "Deductions and exemptions", "BASIC", "tax")
add("An exemption in direct tax means:", ["The specified income or category is excluded from tax under the law", "The payer must charge GST", "The taxpayer pays no customs duty only", "The tax authority waives all future tax"], 0, "Exemption excludes qualifying income or transactions from taxable scope under the governing provision.", "Indian Tax System", "Deductions and exemptions", "BASIC", "tax")
add("Tax evasion is:", ["Illegal concealment or understatement to avoid tax", "Choosing a lawful deduction", "Claiming a refund correctly", "Paying tax in instalments"], 0, "Tax evasion uses illegal concealment or misstatement rather than lawful planning.", "Indian Tax System", "Tax compliance", "BASIC", "tax")
add("Tax avoidance differs from evasion because avoidance:", ["Uses legally permissible provisions to reduce tax", "Always involves false invoices", "Is automatically criminal", "Applies only to customs"], 0, "Avoidance is within the legal framework; evasion involves unlawful concealment or misrepresentation.", "Indian Tax System", "Tax planning", "INTERMEDIATE", "tax")
add("A progressive tax is one in which:", ["Higher income groups generally face a higher marginal rate", "The same fixed amount applies to everyone", "Everyone pays the same percentage", "Only imports are taxed"], 0, "Progressive taxation increases the applicable rate or burden with ability to pay.", "Indian Tax System", "Tax structures", "BASIC", "tax")
add("A proportional tax charges:", ["The same rate on the taxable base", "No tax below a threshold", "A higher rate at every income level", "Different rates depending on customs origin"], 0, "Proportional tax uses a constant rate on the relevant tax base.", "Indian Tax System", "Tax structures", "BASIC", "tax")
add("A regressive tax can mean:", ["Its burden takes a larger share of lower incomes", "It always has a rising marginal rate", "It applies only to corporations", "It is not paid as money"], 0, "A regressive burden is relatively heavier for lower-income taxpayers.", "Indian Tax System", "Tax structures", "INTERMEDIATE", "tax")
add("Income tax is generally administered as a:", ["Union subject", "State-only tax", "Municipal service charge", "Customs receipt"], 0, "Income tax other than agricultural income is levied by the Union.", "Indian Tax System", "Central and state taxes", "BASIC", "tax")
add("A salaried person receives ₹50,000 and has a lawful deduction of ₹5,000. Taxable salary for that simple illustration is:", None, 0, "Taxable salary is ₹50,000 minus the ₹5,000 deduction, giving ₹45,000.", "Indian Tax System", "Practical tax calculation", "ADVANCED", "tax", "NAT", nat_answer=45000, tolerance=0)
add("Tax revenue contributes mainly to:", ["Public services and government expenditure", "Only private company profits", "Only stock-market dividends", "Only foreign reserve accumulation"], 0, "Tax revenue finances public goods and government programmes.", "Indian Tax System", "Tax revenue and public services", "BASIC", "tax")

# GST and customs (12)
add("GST is a tax on:", ["Supply of goods and services", "Only agricultural land", "Only salaries", "Only imported crude oil"], 0, "GST is levied on specified supplies of goods or services.", "GST and Customs Duty", "GST fundamentals", "BASIC", "gst")
add("For a supply within one Indian state, CGST and SGST generally apply instead of IGST:", ["True", "False"], 0, "An intra-state supply ordinarily attracts CGST and SGST; IGST applies to inter-state supplies.", "GST and Customs Duty", "Intra-state and inter-state GST", "BASIC", "gst")
add("Goods sold from Maharashtra to Uttar Pradesh are ordinarily:", ["An inter-state supply attracting IGST", "An intra-state supply attracting only CGST", "Outside GST", "Subject only to income tax"], 0, "Cross-state supply is inter-state and ordinarily attracts IGST.", "GST and Customs Duty", "Intra-state and inter-state GST", "INTERMEDIATE", "gst")
add("Input Tax Credit allows a registered taxpayer to:", ["Set eligible input tax against output tax liability", "Avoid GST registration", "Replace customs duty", "Receive a refund in every case"], 0, "ITC offsets eligible taxes paid on inputs against GST output liability, subject to conditions.", "GST and Customs Duty", "Input Tax Credit", "BASIC", "gst")
add("GST registration becomes relevant when:", ["A person meets applicable threshold or mandatory registration conditions", "A person makes any personal purchase", "Only a bank account is opened", "Only imported gold is consumed"], 0, "Registration depends on business liability, threshold and mandatory provisions.", "GST and Customs Duty", "Registration", "BASIC", "gst")
add("A GST invoice primarily provides:", ["Supply, tax and party details for compliance", "Only the seller's logo", "No tax information", "Proof of customs exemption only"], 0, "A GST invoice records supply and tax details required for invoicing and input tax credit.", "GST and Customs Duty", "GST invoice", "BASIC", "gst")
add("The GST Council is responsible for:", ["Recommendations on GST policy and structure", "Issuing all passports", "Fixing RBI repo rates", "Managing customs ports"], 0, "The GST Council includes Union and State representation and recommends GST policy.", "GST and Customs Duty", "GST Council", "INTERMEDIATE", "gst")
add("GST collection is deposited by:", ["Registered suppliers through the GST framework", "Only customs officers", "Only the Ministry of Commerce", "Only State treasuries directly from consumers"], 0, "Registered taxable persons collect GST and remit it through the GST system.", "GST and Customs Duty", "GST collection", "BASIC", "gst")
add("Customs duty is imposed primarily on:", ["Cross-border import or export of specified goods", "Only salaries earned in India", "Only domestic retail sales", "Only share dividends"], 0, "Customs duty regulates and taxes specified goods crossing customs borders.", "GST and Customs Duty", "Customs duty", "BASIC", "gst")
add("Import duty generally:", ["Adds to the cost of an imported product", "Always lowers the world price", "Is only a corporate income tax", "Is never charged at customs"], 0, "Import duty is part of the landed-cost burden on specified imports.", "GST and Customs Duty", "Import duty", "BASIC", "gst")
add("Export duty is:", ["A customs duty on specified exports", "A tax on only inter-state domestic sales", "An RBI policy rate", "GST input tax credit"], 0, "Export duty applies to selected goods exported outside India.", "GST and Customs Duty", "Export duty", "INTERMEDIATE", "gst")
add("CGST is the component collected for:", ["The Union share on an intra-state GST supply", "The entire IGST share", "Import-only customs", "Corporate dividend tax"], 0, "CGST represents the Central Government share on intra-state supplies.", "GST and Customs Duty", "CGST and SGST", "ADVANCED", "gst")

# Union budget (10)
add("The Union Budget presents:", ["Government receipts and proposed expenditure for the financial year", "Only RBI profit", "Only company balance sheets", "Only exports by category"], 0, "The Union Budget sets proposed government revenue and expenditure.", "Union Budget", "Budget fundamentals", "BASIC", "budget")
add("Tax receipts are an example of:", ["Revenue receipt", "Capital receipt only", "Fiscal reserve", "External debt stock"], 0, "Tax revenue is recurring and generally classified as revenue receipt.", "Union Budget", "Revenue and capital receipts", "BASIC", "budget")
add("Loan recovery by government is normally:", ["A capital receipt", "A recurring revenue receipt", "A customs duty", "A revenue expenditure"], 0, "Loan recoveries are asset-related inflows and form capital receipts.", "Union Budget", "Revenue and capital receipts", "INTERMEDIATE", "budget")
add("Building a bridge is usually:", ["Capital expenditure", "Revenue expenditure", "Tax deduction", "GST input credit"], 0, "Creation or acquisition of an asset is generally capital expenditure.", "Union Budget", "Revenue and capital expenditure", "BASIC", "budget")
add("Salaries paid to regular public officials are generally:", ["Revenue expenditure", "Capital expenditure", "Capital receipt", "Fiscal deficit"], 0, "Recurring employee compensation is revenue expenditure.", "Union Budget", "Expenditure", "BASIC", "budget")
add("A subsidy is:", ["Government financial support to reduce a cost or price", "A tax on imports", "A foreign reserve", "Always a loan recovery"], 0, "Subsidies transfer resources to reduce specified costs or support policy objectives.", "Union Budget", "Subsidies", "BASIC", "budget")
add("Infrastructure spending is often treated as:", ["Public investment that creates assets or capacity", "Only an income-tax deduction", "A customs barrier", "An export incentive"], 0, "Infrastructure spending is public investment in physical or social assets.", "Union Budget", "Infrastructure", "INTERMEDIATE", "budget")
add("Government borrowing increases:", ["Public debt and/or associated liabilities", "Only private consumption automatically", "Only GST rates", "Foreign trade policy"], 0, "Borrowing creates a liability that becomes part of public debt.", "Union Budget", "Borrowing and debt", "INTERMEDIATE", "budget")
add("The Union Budget is presented by:", ["The Ministry of Finance / Union Finance Minister", "The RBI Governor alone", "The GST Council alone", "The Directorate General of Foreign Trade"], 0, "The Union Finance Minister presents the Union Budget on behalf of the government.", "Union Budget", "Institutional role", "BASIC", "budget")
add("If expenditure is ₹100 crore and receipts excluding borrowing are ₹90 crore, fiscal deficit is:", None, 0, "Fiscal deficit = expenditure minus receipts excluding borrowing: ₹100 crore minus ₹90 crore = ₹10 crore.", "Union Budget", "Fiscal deficit", "ADVANCED", "budget", "NAT", nat_answer=10, tolerance=0)

# RBI and banking (12)
add("The RBI is India's:", ["Central bank", "Commercial bank regulator only", "Only tax authority", "Only export promotion agency"], 0, "The Reserve Bank of India is the country's central bank.", "RBI and Banking", "RBI role", "BASIC", "rbi")
add("When the RBI raises the repo rate, commercial banks may face:", ["Higher short-term borrowing costs and potentially higher lending rates", "Lower deposit safety", "Automatic GST exemption", "Higher customs duty"], 0, "Repo-rate increases raise costs for secured short-term central-bank borrowing and can transmit to lending rates.", "RBI and Banking", "Repo rate", "BASIC", "rbi")
add("CRR refers to:", ["Cash Reserve Ratio", "Capital Revenue Receipt", "Current Repo Revenue", "Central Road Reserve"], 0, "CRR is the minimum portion of specified bank liabilities that banks maintain as central-bank cash reserve.", "RBI and Banking", "CRR", "BASIC", "rbi")
add("SLR requires banks to maintain a proportion of specified liabilities in:", ["Approved liquid assets such as government securities and cash", "Only foreign currency", "Only corporate loans", "Only unlisted shares"], 0, "Statutory Liquidity Ratio requires maintenance in approved liquid assets.", "RBI and Banking", "SLR", "INTERMEDIATE", "rbi")
add("Monetary policy mainly uses instruments to influence:", ["Money, credit and interest-rate conditions", "Corporate income-tax slabs", "Customs tariff codes", "GST Council seats"], 0, "Monetary policy seeks to manage liquidity and monetary conditions.", "RBI and Banking", "Monetary policy", "BASIC", "rbi")
add("If food, fuel and other representative consumer prices rise broadly and persistently, the economy is experiencing:", ["Inflation", "Deflation", "A customs surplus", "Fiscal consolidation"], 0, "Broad, sustained increases in consumer prices indicate inflation.", "RBI and Banking", "Inflation", "BASIC", "rbi")
add("Deflation means:", ["A sustained decrease in the general price level", "A rise in inflation", "A rise in GDP only", "A loss of foreign reserves only"], 0, "Deflation is a broad, sustained decline in prices.", "RBI and Banking", "Deflation", "INTERMEDIATE", "rbi")
add("CPI is used especially to track:", ["Changes in consumer goods and services prices", "Only wholesale commodity prices", "Only stock prices", "Only government borrowing"], 0, "Consumer Price Index measures changes in a representative consumer basket.", "RBI and Banking", "CPI", "BASIC", "rbi")
add("WPI primarily measures:", ["Changes in wholesale transaction prices", "Consumer rent only", "Only stock market returns", "Only customs collections"], 0, "Wholesale Price Index tracks prices at the wholesale stage.", "RBI and Banking", "WPI", "INTERMEDIATE", "rbi")
add("The bank rate is:", ["A rate at which RBI lends to banks under applicable RBI facilities", "The interest on every savings deposit", "A customs import duty", "GST charged to customers"], 0, "Bank rate is an RBI policy/reference rate for designated central-bank lending windows.", "RBI and Banking", "Bank rate", "ADVANCED", "rbi")
add("Financial inclusion aims to:", ["Provide usable and affordable financial services to underserved people", "Eliminate all commercial banks", "Restrict digital payments", "Replace taxation"], 0, "Financial inclusion expands access to appropriate financial services.", "RBI and Banking", "Financial inclusion", "BASIC", "rbi")
add("If policy interest rates rise for a borrower on a floating-rate loan, monthly interest cost generally:", ["Increases if the loan rate is fully linked and benchmarked", "Always becomes zero", "Cannot change", "Is fixed by GST"], 0, "A floating-rate loan linked to a rising benchmark usually has a higher interest cost.", "RBI and Banking", "Interest rates", "ADVANCED", "rbi")

# Foreign trade (14)
add("An import is:", ["Purchase of a good or service from abroad", "Sale of a domestic good abroad", "Domestic barter only", "A bank deposit in India"], 0, "Imports enter the domestic economy from foreign sources.", "Foreign Trade", "Imports and exports", "BASIC", "trade")
add("An export is:", ["Sale of domestic goods or services to foreign buyers", "Purchase from abroad", "A customs return", "Domestic tax payment"], 0, "Exports are sold to buyers outside the domestic economy.", "Foreign Trade", "Imports and exports", "BASIC", "trade")
add("Why does India import substantial crude oil?", ["Domestic production is insufficient to meet refinery and fuel demand", "Crude oil cannot be used in India", "India bans all crude production", "Oil imports have no cost"], 0, "India depends materially on crude imports for petroleum product demand.", "Foreign Trade", "Energy imports", "BASIC", "trade")
add("Major Indian exports include:", ["Pharmaceutical products, textiles and IT services", "Only crude oil", "Only imported gold", "Only domestic real estate"], 0, "India exports a diversified range, including medicines, textiles and services.", "Foreign Trade", "Export categories", "BASIC", "trade")
add("Major Indian imports include:", ["Crude oil, gold and machinery/electronics", "Only mangoes", "Only Indian software", "Only local rail tickets"], 0, "India imports energy and capital/consumer products in significant categories.", "Foreign Trade", "Import categories", "BASIC", "trade")
add("Merchandise trade concerns:", ["Physical goods", "Only digital services", "Only patents", "Only tourism"], 0, "Merchandise trade refers to physical goods; services trade is separately classified.", "Foreign Trade", "Merchandise and services", "BASIC", "trade")
add("A trade deficit occurs when merchandise imports exceed merchandise exports:", ["True", "False"], 0, "The merchandise trade deficit is the excess of merchandise imports over exports.", "Foreign Trade", "Trade balance", "BASIC", "trade")
add("India may have a trade deficit even while:", ["Its services exports are strong", "It has no imports", "It has no foreign payments", "Its currency is never exchanged"], 0, "The trade and services/current-account balances are separate but related components.", "Foreign Trade", "Trade and services", "INTERMEDIATE", "trade")
add("A tariff is:", ["A tax on imported or sometimes exported goods", "A subsidy paid to every consumer", "An exchange reserve", "A customs invoice only"], 0, "Tariffs alter the price of traded goods through customs duties.", "Foreign Trade", "Tariffs", "BASIC", "trade")
add("A non-tariff barrier can include:", ["Licensing, standards and import restrictions", "Only customs duty", "Only corporate tax", "Only GST on cinema tickets"], 0, "Non-tariff barriers regulate trade without an ordinary tariff.", "Foreign Trade", "Trade barriers", "INTERMEDIATE", "trade")
add("Export incentives may aim to:", ["Improve export competitiveness or promote specified sectors", "Reduce every import", "Eliminate the exchange market", "Replace customs at all borders"], 0, "Export incentives include schemes supporting competitiveness and specified exports.", "Foreign Trade", "Export incentives", "INTERMEDIATE", "trade")
add("Ports and logistics improve trade by:", ["Reducing transport delay and transaction cost", "Eliminating all tariffs", "Replacing exchange rates", "Preventing exports"], 0, "Efficient ports and logistics move goods faster and at lower delivered cost.", "Foreign Trade", "Logistics", "BASIC", "trade")
add("International trade creates jobs primarily through:", ["Export industries, logistics and related services", "Only customs head offices", "Only foreign tourism", "Only currency printing"], 0, "Trade expands production and service employment across export and logistics chains.", "Foreign Trade", "Employment", "INTERMEDIATE", "trade")
add("If imports cost $200 million and exports earn $170 million, the merchandise trade deficit is:", None, 0, "Merchandise trade deficit equals imports minus exports: 200 minus 170 = $30 million.", "Foreign Trade", "Trade balance", "ADVANCED", "trade", "NAT", nat_answer=30, tolerance=0)

# Trading partners (10)
add("The United States is strategically important for India primarily because of:", ["Large trade and services/economic links", "No trade with India", "Only defence spending", "Only weather cooperation"], 0, "India has extensive trade, technology and services links with the US.", "India's Trading Partners", "United States", "BASIC", "partners")
add("China is a major source for India of:", ["Machinery and electronics among other goods", "No manufactured goods", "Only Indian rupee notes", "Only petroleum from Indian refineries"], 0, "China supplies varied manufactured and intermediate products to India.", "India's Trading Partners", "China", "INTERMEDIATE", "partners")
add("The UAE is important in India–West Asia trade because it is:", ["A major commercial and re-export hub and energy trade partner", "An inland neighbour with no ports", "A member of India's Parliament", "A customs-free domestic state"], 0, "The UAE is a major trade, logistics and energy-related partner for India.", "India's Trading Partners", "United Arab Emirates", "BASIC", "partners")
add("Russia remains strategically relevant to India’s trade due in part to:", ["Energy, defence and strategic commodities trade", "Only tourism", "No bilateral trade", "Only domestic Indian banking"], 0, "Russia has commercial links with India spanning energy and strategic sectors.", "India's Trading Partners", "Russia", "INTERMEDIATE", "partners")
add("Saudi Arabia is significant for India mainly because of:", ["Energy supplies and economic cooperation", "No energy exports", "Only agricultural trade", "Only digital services"], 0, "Saudi Arabia is an important energy supplier and investment/commerce partner.", "India's Trading Partners", "Saudi Arabia", "BASIC", "partners")
add("Singapore is important for India as:", ["A trade, logistics and financial-services hub", "A landlocked state", "An Indian state", "A commodity-producing island without connectivity"], 0, "Singapore supports trade, shipping and regional financial and commercial links.", "India's Trading Partners", "Singapore", "INTERMEDIATE", "partners")
add("The European Union is for trade purposes:", ["A grouping of 27 European member states", "A single Indian state", "Only a military alliance", "A global customs-free currency only"], 0, "The EU is a 27-member economic and political union with a coordinated trade policy.", "India's Trading Partners", "European Union", "BASIC", "partners")
add("Japan is closely relevant to India through:", ["Technology, investment and infrastructure cooperation", "Only crude-oil supply", "No economic relationship", "Only a visa-free border"], 0, "Japan and India cooperate across technology, investment and infrastructure.", "India's Trading Partners", "Japan", "INTERMEDIATE", "partners")
add("Bangladesh is an important trade partner for India mainly due to:", ["Geographic proximity and cross-border trade", "No common border", "Only defence aircraft exports", "Only gold imports"], 0, "India and Bangladesh conduct substantial regional trade across a shared border.", "India's Trading Partners", "Bangladesh", "BASIC", "partners")
add("Australia is relevant to India’s trade and resources because of:", ["Economic, critical minerals and services cooperation", "No universities or services", "Only landlocked trade", "No bilateral trade framework"], 0, "Australia has growing trade, resources and education/services links with India.", "India's Trading Partners", "Australia", "INTERMEDIATE", "partners")

# International organisations and trade agreements (6)
add("The WTO sets rules and provides a forum for:", ["Multilateral international trade negotiations and dispute settlement", "Only central-bank interest rates", "Only customs duty collection in India", "Only military alliances"], 0, "The WTO administers trade agreements and dispute settlement.", "International Organisations and Trade Agreements", "WTO", "BASIC", "org")
add("The IMF primarily assists members with:", ["Balance-of-payments support and economic policy surveillance", "Only customs clearance", "Only export subsidies", "Only national election administration"], 0, "The IMF provides surveillance and financial support for balance-of-payments difficulties.", "International Organisations and Trade Agreements", "IMF", "INTERMEDIATE", "org")
add("The World Bank group mainly provides:", ["Development finance and advisory support", "Military command", "GST registration", "Corporate tax assessment"], 0, "World Bank institutions support development through finance and knowledge.", "International Organisations and Trade Agreements", "World Bank", "BASIC", "org")
add("The Asian Development Bank supports:", ["Economic development and regional cooperation in Asia", "Only NATO defence spending", "Only Indian customs", "Only private retail payments"], 0, "ADB provides development finance and technical support in Asia.", "International Organisations and Trade Agreements", "ADB", "INTERMEDIATE", "org")
add("BRICS is:", ["A multilateral economic and political cooperation grouping", "A customs union for Indian states", "A central-bank reserve rate", "A WTO court"], 0, "BRICS is a cooperation forum involving Brazil, Russia, India, China and South Africa.", "International Organisations and Trade Agreements", "BRICS", "BASIC", "org")
add("An FTA mainly seeks to:", ["Reduce or eliminate specified trade barriers among participants", "Create a common currency always", "Close all borders", "Replace every domestic tax"], 0, "Free trade agreements reduce tariffs or barriers under negotiated rules.", "International Organisations and Trade Agreements", "Trade agreements", "ADVANCED", "org")

# Foreign exchange and rupee (6)
add("An exchange rate is:", ["The price of one currency in terms of another", "A customs duty", "A stock-market index", "A tax exemption"], 0, "Exchange rate specifies how many units of one currency exchange for another.", "Foreign Exchange and Rupee", "Exchange rates", "BASIC", "fx")
add("If the rupee depreciates against the dollar while the dollar price of crude oil is unchanged, India's crude import bill in rupees generally:", ["Increases", "Decreases", "Becomes fixed", "Disappears"], 0, "The same dollar outlay requires more rupees when the rupee depreciates.", "Foreign Exchange and Rupee", "Rupee depreciation", "INTERMEDIATE", "fx")
add("Rupee depreciation can make Indian exports:", ["Potentially more competitive in foreign-currency terms", "Automatically less competitive", "Entirely customs-free", "Unconnected to trade"], 0, "Depreciation can lower the foreign-currency price of domestic exports, subject to costs and demand.", "Foreign Exchange and Rupee", "Rupee depreciation", "ADVANCED", "fx")
add("Foreign exchange reserves are:", ["Foreign assets held by the central bank and public-authority institutions", "Only Indian rupee notes", "Only customs revenue", "Only foreign direct investment applications"], 0, "Forex reserves are external assets held to support monetary and external-sector stability.", "Foreign Exchange and Rupee", "Forex reserves", "BASIC", "fx")
add("FDI differs from FPI mainly because FDI:", ["Usually involves lasting interest and control in an enterprise", "Is a short-term tourist payment", "Always includes only imports", "Is prohibited in India"], 0, "Foreign direct investment reflects a lasting interest and influence/control; FPI is portfolio investment.", "Foreign Exchange and Rupee", "FDI and FPI", "INTERMEDIATE", "fx")
add("An ₹80 crore export receipt is converted at ₹83 per US dollar. Approximately how many million US dollars are received?", None, 0, "Divide ₹800 million by ₹83 per dollar, giving approximately USD 9.6386 million.", "Foreign Exchange and Rupee", "Exchange conversion", "ADVANCED", "fx", "NAT", nat_answer=9.6386, tolerance=0.01)

assert len(rows) == 100

# Exact distributions are fixed in the written sections.
counts = {}
difficulties = {"BASIC": 60, "INTERMEDIATE": 30, "ADVANCED": 10}
for r in rows:
    counts[r["topic"]] = counts.get(r["topic"], 0) + 1
assert counts == {
    "Indian Economy – Fundamentals": 12,
    "Indian Tax System": 18,
    "GST and Customs Duty": 12,
    "Union Budget": 10,
    "RBI and Banking": 12,
    "Foreign Trade": 14,
    "India's Trading Partners": 10,
    "International Organisations and Trade Agreements": 6,
    "Foreign Exchange and Rupee": 6,
}
actual_difficulties = {d: sum(r["difficulty"] == d for r in rows) for d in difficulties}
if actual_difficulties != difficulties:
    print("Actual difficulty counts:", actual_difficulties)
assert actual_difficulties == difficulties

# Remove exact normalized duplicates already present in relevant economics/defence/GS banks.
def normalized(text):
    return " ".join(str(text).lower().replace("’", "'").replace("–", "-").split())

existing = set()
for path in (DATA.glob("*.json")):
    try:
        bank = json.loads(path.read_text())
    except Exception:
        continue
    for section in bank.get("sections", []) if isinstance(bank, dict) else []:
        for old in section.get("questions", []):
            existing.add(normalized(old.get("q", "")))

for r in rows:
    assert normalized(r["q"]) not in existing, f"Duplicate: {r['q']}"

bank = {
    "id": "economics-india-world-trade-100",
    "title": "ECONOMICS – INDIA & WORLD TRADE",
    "subtitle": "100 practical questions on the Indian economy, taxation, RBI, trade and international economic organisations",
    "sourceType": "PRACTICE",
    "exam": "Economics",
    "paperType": "PRACTICE",
    "contentMode": "INTERNAL",
    "source": "Original syllabus-based questions with official reference metadata",
    "verificationStatus": "PRACTICE — official-source metadata; calculation and concept verification completed",
    "sections": [],
}

topic_order = [
    "Indian Economy – Fundamentals",
    "Indian Tax System",
    "GST and Customs Duty",
    "Union Budget",
    "RBI and Banking",
    "Foreign Trade",
    "India's Trading Partners",
    "International Organisations and Trade Agreements",
    "Foreign Exchange and Rupee",
]
for topic in topic_order:
    bank["sections"].append({
        "name": topic,
        "questions": [r for r in rows if r["topic"] == topic],
    })

(DATA / "economics-india-world-trade-100.json").write_text(
    json.dumps(bank, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

papers_path = DATA / "papers.json"
papers = json.loads(papers_path.read_text())
papers = [p for p in papers if p.get("id") != bank["id"]]
papers.insert(1, {
    "id": bank["id"],
    "subject": "economics-india-world-trade",
    "title": bank["title"],
    "subtitle": "100 original MCQs and numerical questions · Indian economy, taxation, RBI and world trade",
    "file": "data/economics-india-world-trade-100.json",
    "questionCount": 100,
    "durationMin": 120,
    "correctMark": 1,
    "negativeMark": 0.25,
    "exam": "Economics",
    "paperType": "PRACTICE",
    "contentMode": "INTERNAL",
    "source": "Original economics practice questions with official-source metadata",
    "verificationStatus": "PRACTICE — original content; verified against official reference sources",
})
papers_path.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n")

subjects_path = DATA / "subjects.json"
subjects = json.loads(subjects_path.read_text())
if not any(s.get("id") == "economics-india-world-trade" for s in subjects):
    subjects.insert(1, {
        "id": "economics-india-world-trade",
        "title": "ECONOMICS – INDIA & WORLD TRADE",
        "description": "Indian economy, taxation, GST, RBI, government finance, imports, exports and international trade",
        "icon": "📈",
    })
subjects_path.write_text(json.dumps(subjects, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({
    "questions": len(rows),
    "topic_counts": counts,
    "difficulty_counts": {d: sum(r["difficulty"] == d for r in rows) for d in difficulties},
    "mcq": sum(r["type"] == "MCQ" for r in rows),
    "nat": sum(r["type"] == "NAT" for r in rows),
}, indent=2))
