import re, tkinter, os, sys, traceback, json

unworking_string = '''248429,140,Senior Product Manager – Mobile App (H/F),,Sébastien WEISSE,,766,1,1,,0,0,"<p>Within the Digital &amp; Data office for Soprema Group, the senior digital product manager is ultimately responsible for the successful delivery and lifecycle of digital solutions for customers. The purpose of the position is to work worldwide with business stakeholders to define and create customer value added solutions mainly for mobile touchpoints.</p><p>Depending on success and growth of the first initiatives, the position might evolve to a Head of digital factory.</p><p>Objectives of this Role:</p><p><strong>1. Product Discovery</strong></p><ul><li>Conduct user research and usability studies, collaborating with designers, developers’ teams from end to end of the process</li><li>Collect users and customers insights via interviews and workshops to identify value added features</li><li>Understand your users pain points and needs through qualitative research or quantitative data</li><li>Analyze your product usage through our analytical tools to understand what drives usage and conversion</li></ul><p><strong>2. Product Strategy</strong></p><ul><li>Build and nurture the product vision and convert it into concrete strategy</li><li>Turn that into a strategy and a well-thought roadmap</li><li>Partner with business owners, IT architects and agile product teams to incorporated it into the company digital product portfolio plan</li><li>Make sure your team and stakeholders understand and embrace it through your engaging communication</li><li>Integrate your group product strategy within the company digital strategy</li></ul><p><strong>3. Product Delivery</strong></p><ul><li>Transform business requirements into functional &amp; technical requirements</li><li>Determine, consolidate, prioritize customers and user requests into a Product Backlog considering feasibility, viability, and desirability</li><li>Oversee, manage and lead requirements discovery, solution design, user story writing, feature development, and user acceptance testing</li><li>Partner with the architecture teams to identify key capabilities needed as well as identifying potential issues</li><li>Partner with cross functional teams regularly to ensure alignment on feature development and prioritization</li><li>Ensure that all products shipped by your team are bug-free</li><li>Test hypothesis and ideas on the field with ingenious MVPs</li><li>Set up and monitor performance indicators for the digital solutions</li><li>Analyse features performance through A/B testing, behavior data, etc. and generate insights about your product</li></ul><p><strong>4. Project Lead</strong></p><ul><li>Lead all projects stakeholders in a consistent product approach (discovery, development, roll out): Business Owner, IT, Data expert, UX/CX expert, process owner, agile development team,</li><li>Apply agile development principles, set up or use appropriate project management tools</li><li>Set foundations and structure for a digital factory organization.</li></ul>","<p>SOPREMA is a French group with an international dimension (€3.08 billion , 8,400 employees), a leader in the production and installation of waterproofing systems for construction.</p><p>To strengthen our team, we are looking to a:</p><p style=""text-align: center;""><strong>Senior Product Manager – Mobile App (H/F)</strong></p>","<p><strong>You are:</strong></p><ul><li>Graduated Engineer, Master of Science Degree in computer science of Information system or Business School</li><li>5-10 years’ experience in digital product management preferably in B2B environment and min 3 years’ experience with mobile application.</li><li>Passionate about building great products and solving customer and business problems</li><li>Analytical and “customer centric” person, convinced that data could help to drive your product strategy</li><li>Fluent in English</li></ul><p><strong>You have:</strong></p><ul><li>Knowledge of the world of mobile and effective application strategy: acquisition techniques, ASO, analytics m-crm</li><li>Experience with digital platform ecosystems (eCommerce, Marketplace, IoT, API)</li><li>Experience in project management and strong ability to orchestrate competencies and expertise in cross-functional team (UX, Data, Architecture, Marketing).</li><li>Doer mindset with ability to thrive in scale up environment growing fast.</li><li>Thoughtful and natural ability to get things done. You qualify as an “achiever”.</li><li>Strong communication capabilities to federate and facilitate dialog between IT/ technical teams and business or supply chain team.</li></ul><p><strong>It would a plus if you have:</strong></p><ul><li>Usability design experience</li><li>Certification on an Agile Project Management Methodology</li><li>Experience with back-end and front-end programming languages</li></ul>",True,2021-07-29 00:00:00,2021-07-29 11:02:38,,False,False,False,91,STRASBOURG,False,48.58293,7.74375,,67000,Strasbourg,FR,,False,2,2,24946437,https://services.multiposting.fr/v3/import/offers/24946437/delegation/7e347d49debe0d7d5af279cf29dcc75256443f4b53fb4ee03de3059b0dee2135,457d748ee2d3eb2f10a8dd72dbc0fa4270644828,True,,'''
header = "Id,IdOrganisation,Title,Reference,Client,IdClientChoice,IdResponsable,IdContrat,Status,Type,Length,UnitTemp,DescriptionPost,DescriptionEnterprise,DescriptionProfil,Wysiwyg,DateCreate,LastStatusModificationDate,AddQuestionnaire,QuestionnaireForCandidate,QuestionnaireRequiredForRecruiter,AssessfirstForCandidate,IdProcess,Location,DefaultJob,Latitude,Longitude,Address,ZipCode,Town,Country,Notes,NotesAsHtml,CvRequired,CoverRequired,MultipostingOffer,MultipostingLink,MultipostingNotifyToken,MultipostingValidated,VisiotalentRecruitmentToken,EasyrecrueCampaignId"

def list_04a5489ea4f0(string):
    string_list = [x for x in string]
    lever = True
    for i in range(len(string_list)):
        if string_list[i] == '"':
            lever = not lever
        if string_list[i] == "," and lever:
            string_list[i] = "04a5489ea4f0"
    return "".join(string_list).split("04a5489ea4f0")

l_un_str = list_04a5489ea4f0(unworking_string)
l_header = list_04a5489ea4f0(header)

with open("248429.txt", "w") as file_248429:
    my_dict = dict(zip(l_header, l_un_str))
    start = 0
    finish = 0
    description_post = my_dict["DescriptionPost"]
    description_profile = my_dict["DescriptionProfil"]
    if description_post[0] == '"':
        description_post = description_post[1:]
    if description_post[-1] == '"':
        description_post = description_post[:-1]
    if description_profile[0] == '"':
        description_profile = description_profile[1:]
    if description_profile[-1] == '"':
        description_profile = description_profile[:-1] 
    file_248429.write(description_post)
    file_248429.write("\n<br>\n")
    file_248429.write(description_profile)
    

