import streamlit as st
st.title('''CDMP Practice Questions''')

# Define the quiz questions and answers
quiz_data_1 = [
    {
        "question": "Data is an organizational asset. What international standard is concerned with asset management?",
        "options": [
            "ISO 27001",
            "ISO 8000",
            "ISO 55000/55001",
            "ANSI 859",
            "ISO 25000"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "According to the DMBOK, which of the following are included as Data Management goals?",
        "options": [
            "Big Data goals need to change to reflect reality",
            "We should ensure that data can be used effectively to add value to the enterprise.",
            "Data Quality goals must be aligned with ISO27001",
            "Data Management goals should be driven by technical capability and available capabilities",
            "Data Management goals must focus first on legislation"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "In the data lifecycle, the DMBoK recommends minimizing ROT data. ROT stands for?",
        "options": [
            "Data that is Redundant, Obsolete, Trivial",
            "Data that is not Relational, Operational, Timely",
            "Data that is not Requested, Orchestrated, Technology supported.",
            "Data that is not Realistic, Ordered, Timely",
            "Data is Routine, Obsolete, Tiny"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Information is:",
        "options": [
            "Always stored in a computer systems",
            "A management discipline",
            "A byproduct of IT systems.",
            "Data in context"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Data differs with regards to other assets because",
        "options": [
            "It uses automation",
            "It is regulated",
            "It has value",
            "It can be used yet still retain value",
            "It is big"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which is a valid Environmental component of data management?",
        "options": [
            "Motivation",
            "Practices & Techniques",
            "Hardware Management",
            "Database Management.",
            "Project Management"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of these is not a Knowledge Area in DMBoK v2?",
        "options": [
            "Data Governance",
            "Master & Reference Data Management",
            "Data Quality Management",
            "Big Data & Data Science.",
            "Data Security Management"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "The Data Management Body of Knowledge is produced by?",
        "options": [
            "The Data Management Association.",
            "The Data Analysis Association",
            "The Data Practitioner Association",
            "The Project Management Institute",
            "The Data Management Authority"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "According to the DMBoK, which is not a component of a Data Management strategy?",
        "options": [
    "A draft implementation roadmap with projects and action items.",
    "A compelling vision for Data Management",
    "Identifying individuals for Data Management roles",
    "Descriptions of Data Management roles and organizations, along with a summary of their responsibilities and decision rights",
    "A summary business case for Data Management with selected examples"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The right to be forgotten is",
        "options": [
            "A person's right to change their name.",
            "A person's right to have all their information erased from an organization",
            "A person's right to have imperfect memory",
            "A person's right for all search criteria not to lead to their details",
            "A person's right to have their information removed from all databases on earth"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is not included in the opinion of the European Data Protection Supervisor (EDPS) on data ethics?",
        "options": [
            "Future-oriented regulation of data processing and respect for the rights to privacy and to data protection",
            "Privacy-conscious engineering and design of data processing products and services",
            "Accountable controllers who determine personal information processing",
            "Empowered individuals",
            "Right to request removal of personal data"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "According to the DMBoK2, which items are not a consideration in a data valuation?",
        "options": [
            "has the same stages as the Systems Delivery Lifecycle",
            "Impact to the organization if data were missing",
            "How much we can be ransomed for by a malware attack.",
            "Benefits of higher quality data",
            "What the data could be sold for"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "According to the DAMA DMBoK, the Data Governance Council (DGC) is the highest-authority organization for Data Governance in an organization. Who should typically chair this Council?",
        "options": [
            "The chair should rotate across Data Owners",
            "Any executive/c-level participant in the DGC.",
            "The Chief Information Officer (CIO)",
            "Chief Data Steward (Business)/Chief Data Officer",
            "The Chief Data Architect"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "What are the primary responsibilities of a data steward?",
        "options": [
            "The data analyst who is the subject matter expert (SME) on a set of reference data.",
            "A business role appointed to take responsibility for the quality and use of their organization's data assets",
            "Analysing Data Quality",
            "The manager responsible for writing policies and standards that define the Data Management program for an organization",
            "Identifying data problems and issues"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of these are NOT true of Data Governance?",
        "options": [
            "A DG initiative should always be led by the IT Department",
            "DG is a continuous process of data improvement",
            "IT is a key stakeholder in DG",
            "DG is the exercise of authority and control over the management of data assets.",
            "There are different organization models for DG"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Who is most responsible for communicating and promoting awareness on the value of Data Governance in the organization?",
        "options": [
            "Data stewards",
            "The Chief Executive Officer",
            "Senior Management Executive Forum",
            "Everyone in the Data Management community.",
            "Central Communications and Corporate Awareness"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "When new governmental and industry regulations are formulated and enacted, Data Governance plays a key role in the process of identifying the data and information components for compliance. What is the most important role in any regulatory compliance project?",
        "options": [
            "Create a Data Governance 'in-house' project with a team of Data Stewards to create a standard response",
            "Work in isolation and mine the data and information for compliance and non-compliance issues",
            "Provide access to any possible data set to the compliance team and allow them to mine the data for non-compliance",
            "Take no part in any project at all, declaring it an audit and risk project.",
            "Working with business and technical leadership to find the best answers to a standard set of regulatory compliance questions (How, Why, When, etc)"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Communicating the value of Data Governance can be approached in a number of ways. Which of the following approaches is NOT a recognized way of doing this?",
        "options": [
            "Providing only negative communications on ongoing data issues to key executive stakeholders",
            "Creating a series of 'elevator pitches' for the appropriate audience.",
            "Maintaining an intranet website",
            "Publishing a regular newsletter via hardcopy or email",
        "Promoting participation in a DM forum or community"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The Data Governance Steering Committee is best described as?",
        "options": [
            "The representatives of data use on project steering committees",
            "The local or divisional council working under auspices of the CDO",
            "The community of interest focused on specific subject areas or projects",
            "The primary and highest authority responsible for the oversight and support of Data Governance activities.",
            "A burden to the agile delivery in a modern enterprise"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "When considering a Data Governance program, communication is a key element. There are many ways of managing this communication, with one of the most effective being a Data Management intranet. Which of the following would you typically NOT put onto such an communication vehicle?",
        "options": [
            "Description of the DG organization, its key members, and contact details",
            "Raw data results of an investigation into a possible data privacy breach",
            "Executive message regarding significant Data Management issues",
            "The Data steward team profiles",
            "Link to a 'raise an issue' log."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Every enterprise is subject to many governmental and industry regulations, many of which regulate how data and information are used and managed. Part of the Data Governance function is to:",
        "options": [
            "Monitor and ensure that organizations meet any regulatory compliance requirements",
            "Enforce enterprise-wide mandatory compliance to regulations",
            "This is about data. Data Governance is accountable for the whole process, with risk and audit reporting to Data Governance.",
            "This is a risk and audit responsibility; Data Governance plays no role in this",
            "Perform ad-hoc audits of possible regulations to report to the Data Governance Council on an information-only basis"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What organization structure should set the overall direction for Data Governance?",
        "options": [
            "Data Quality Board",
            "Data Governance Office",
            "Data Governance Council",
            "PMO",
            "IT Leadership Team"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "In the common enterprise architecture model coded BIAT, the 'I' stands for?",
        "options": [
            "Information",
            "Identification",
            "Integration",
            "Interoperability",
            "Instance"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Data flows can be represented by",
        "options": [
            "Two-dimensional matrices showing the relationships between data entities and data quality.",
            "Two-dimensional matrices showing the relationships between data users and business processes",
            "Two-dimensional matrices showing the relationships between data entities and business processes",
            "Two-dimensional matrices showing the relationships between data users and data consumers",
            "Two-dimensional matrices showing the relationships between data facts and data dimensions"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "An enterprise data model would be composed of",
        "options": [
            "Conceptual models, logical models, and physical models",
            "Conceptual models, subject area models, and logical models",
            "Enterprise models, data models, and compositional models.",
            "Logical models, physical models, and infrastructure models",
            "Conceptual models, star schema models, and interface models"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "An organization's data model contains information (metadata) about which of the following?",
        "options": [
            "Surrogate keys.",
            "Information an organization is interested in",
            "All information available both inside and outside the organization",
            "Information about physical attributes",
            "Only the information needed for Data Governance"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The key architecture domains include",
        "options": [
            "business, data, application, and technology architectures",
            "Zachman, TOGAF, COBIT, and Health architectures",
            "business, strategy, application, and technology architectures",
            "business, data, infrastructure, and technology architectures",
            "process, database, software, and technology architectures."
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The implementation of data architecture exposes the transformation of data as it moves across the landscape. A common name for this concept is:",
        "options": [
            "data modelling",
            "extract, transformation and load",
            "data interfacing",
            "data discovery",
            "data lineage"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "A data architect is best deployed",
        "options": [
            "to build the database solution.",
            "during the early stages of a project to define and shape a strategic solution",
            "after the project completes to identify weaknesses and lessons learned",
            "by project managers to sign off all data deliverables",
            "to manage the delivery of all the data aspects of a program"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "When a project specification is reviewed by the enterprise data architect, which of the following is not a consideration?",
        "options": [
            "Whether enterprise-wide entities conform to agreed standards",
            "What entities in the requirements should be included back into the overall enterprise Data Architecture",
            "Whether entities on individual screens and reports align with the database",
            "Whether to reuse existing or develop new data delivery architectures .",
            "Whether entities and definitions need to be generalized or improved to handle future trends"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The role of the Physical data model in the Metadata repository is",
        "options": [
            "To describe how and where our data is stored on our systems applications or packages",
            "Which version of COTS software (E.g. SAP) is implemented",
            "When the duplicated records were merged.",
            "What the business definition of data concepts is",
            "How many master data records are stored in our MDM system"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The role of the Conceptual data model in the Metadata repository is",
        "options": [
            "To agree the cardinality and optionally of relationships between all entities",
            "To summarize the key data subjects areas for a business area at a high level of abstraction to enable the major data concepts to be understood",
            "To determine the primary, alternate and foreign keys of entities",
            "None of these.",
            "All of these"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Identify who has primary responsibility for data capture and usage design within programs.",
        "options": [
            "Business Data Stewards, Subject Matter Experts (SMEs)",
            "DM Executives, BI Analysts, Data Security Administrator",
            "Data Architects, Data Analysts, Database Administrators",
            "Suppliers, Consumers.",
            "Software Architects, Developers"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What are relationship labels?",
        "options": [
            "A non-identifying relationship.",
            "The nullability setting on a foreign key",
            "A foreign key that has been role-named",
            "The verb phrases describing the business rules in each direction between two entities",
            "A relationship without cardinality"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of these statements has the most meaningful relationship label?",
        "options": [
            "An order is composed of order lines.",
            "An order line contains orders",
            "An order is associated with order lines",
            "An order is related to order lines",
            "An order is connected with order lines"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "All of the following are TRUE statements on relationship types except",
        "options": [
            "A many-to-many relationship says that an instance of each entity may be associated with many instances of the other entity, and vice versa",
            "A one-to-one relationship says that a parent entity may have one and only one child entity.",
            "A one-to-many relationship says that a parent entity may have one or more child entities",
            "A one-to-many relationship says that a child entity may have one or more parent entities",
            "A recursive relationship relates instances of an entity to other instances of the same entity"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "In Dimensional data models, which of these is NOT true regarding Measures?",
        "options": [
            "Measures are found in Fact tables",
            "Just because a value is numerical does not mean it is a measure.",
            "Measures should be numeric and additive",
            "Measures can always be added across all dimensions",
            "Care must be taken if a measure is a snapshot figure"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "In a non-identifying relationship",
        "options": [
            "The primary key of the child entity is concatenated",
            "The primary key of the parent entity becomes a foreign key in the child entity",
            "The foreign key of the parent entity migrates to the child entity",
            "The primary key of the parent entity becomes part of the primary key of the child entity",
            "The primary key of the child entity is removed."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of these is NOT a type of key found in a data model?",
        "options": [
            "Alternate Key",
            "Primary Key",
            "Surrogate Key",
            "Foreign Key",
            "Local Key"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "In the conceptual data model an instantiation of a particular business entity is described as",
        "options": [
            "Dataset",
            "Entity occurrence",
            "Record",
            "Rule",
            "Row"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "In a recursive relationship",
        "options": [
            "The relationship could be an identifying relationship",
            "The relationship could be mandatory at either end",
            "The foreign key must have a role name to avoid attribute duplication.",
            "None of these, recursive relationships are not allowed in Data Models",
            "All of the above"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The highest level of these data model types is the",
        "options": [
            "Conceptual Model",
            "Dimensional model",
            "Physical model",
            "Database model",
            "Logical model"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which approach is considered most effective when supporting multi-dimensional business report requests?",
        "options": [
            "OLAP",
            "OLTP",
            "ODS",
            "BI",
            "EDI"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The acronym ACID stands for",
        "options": [
            "Atomicity, Consistency, Independence, Dominance",
            "Additive, CAP, Independence, Database",
            "Atomicity, Consistency, Isolation, Durability.",
            "Atomicity, Cardinality, Instance, Durability",
            "Arity, Cardinality, Instance, Development"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "When defining your business continuity plan, which of the following should one consider doing?",
        "options": [
            "Make sure that the data is retained sufficiently long, check that critical data is encrypted, check access rights",
            "Consider written policies and procedures, impact mitigating measures, required recovery time and acceptable amount of disruption, the criticality of the documents",
            "Write a report and discuss with management the required budget",
            "Determine the risk, probability and impact, check document backup frequency",
            "Have the contracts in place to acquire new hardware in case of technical problems, define policies"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following should a DBA (database administrator) do if a database schema change is failing?",
        "options": [
            "Call IT support to restore a previous version of the database",
            "Instruct the software designer to refer to the script and re-run it",
            "Remove all the content of the tables and try again",
            "Call the software vendor of the database for technical support",
            "Apply the backout plan to restore a consistent database state"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "If two data stores are able to be inconsistent during normal operations, then the integration approach is",
        "options": [
            "Uncontrolled",
            "Faulty",
            "Synchronous",
            "Asynchronous",
            "Streaming"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Data that is used infrequently or not at all may be moved to an alternative data store. This is called",
        "options": [
            "replication",
            "archiving",
            "analysis",
            "authentication",
            "auditing"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following activities are performed by data operations staff?",
        "options": [
            "Tune the file systems",
            "Implement and control database environments, plan for data retention, keep track of database licenses, monitor and tune database performance",
            "Grant access to tables and rewrite SQL statements",
            "Manage the tape libraries",
            "Clean data that is of bad quality"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The goals of data operations include which of the following",
        "options": [
            "Assuring backups are taken, managing the performance of SQL, and checking data quality",
            "Assuring the performance of the network and storage devices, the quality of the SQL statements, and the selection of DBMS platform",
            "Providing the right database access rights, solving software bugs, and managing database logs",
            "Assuring the quality of the structured data assets, taking backups, and managing the security of the database",
            "Assuring availability of the data throughout its lifecycle, protection, and integrity assurance of structured data assets, and performance optimization of database transactions"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Obfuscation or redaction of data is the practice of?",
        "options": [
            "Making information available to the public",
            "Reducing the size of large databases",
            "Selling data",
            "Making information anonymous or removing sensitive information.",
            "Organizing data into meaningful groups"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of these are increasingly driving legislation for information security and data privacy?",
        "options": [
            "A recognition of Ethical issues in information management",
            "A desire for economic protectionism",
            "ANSI 859",
            "A resistance to open data and transparency",
            "An objective of making life more challenging for information management professionals"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Definition of Data Security Policies should be",
        "options": [
            "Determined by external Regulators.",
            "A collaborative effort between Business and IT",
            "Reviewed by external Regulators",
            "Conducted by external consultants",
            "Based on defined standards and templates"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the role of the Data Governance Council in defining an Information Security policy?",
        "options": [
            "The Data Governance Council should review and approve the high-level Data Security Policy.",
            "The Data Governance Council should define the Data Security Policy",
            "The Data Governance Council should implement the Data Security Policy",
            "The Data Governance Council should draft early versions of the Data Security Policy",
            "The Data Governance Council should have no role in Data Security"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of these are characteristics of an effective data security policy?",
        "options": [
            "The defined procedures are tightly defined, with rigid and effective enforcement sanctions, and alignment with technology capabilities.",
            "The defined procedures ensure that the right people can use and update data in the right way, and that all inappropriate access and update is restricted",
            "The policies are specific, measurable, achievable, realistic, and technology aligned",
            "The procedures defined are benchmarked, supported by technology, framework based, and peer reviewed",
            "None of these"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A RACI matrix is a useful tool to support the _______ in an outsourced arrangement.",
        "options": [
        "Transfer of access controls",
        "Alignment of Business goals",
        "Attributing Costs",
        "Segregation of duties",
        "Service level Agreement"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Stakeholders whose concerns must be addressed in data security management include",
        "options": [
            "The Internal Audit and Risk committees of the organisation",
            "Media analysts, Internal Risk Management, Suppliers, or Regulators",
            "External Standards organisations, Regulators, or the Media",
            "Clients, Patients, Citizens, Suppliers, or Business Partners",
            "All of these."
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "How does Data Security contribute to competitive advantage?",
        "options": [
            "Data Security makes it harder for your competitors to find out about who you do business with",
            "Data Security makes your competitors invest more effort into trying to find out your trade secrets",
            "Governments do not allow organisations to trade if they do not manage Data Security",
            "Data security stops organisations going out of business due to an information leak",
            "Data Security helps to protect proprietary information and intellectual property, as well as customer and partner information"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "The needs of data protection require us to ensure that",
        "options": [
            "Data is secured with a password",
            "Data is processed only in ways compatible with the intended and communicated use it was collected for, and respects the consent of the data subject",
            "Data can always be freely used in the company as it is a company asset",
            "Data is frequently backed up so that it can be recovered in all cases",
            "Data is encrypted at all times"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Apart from security requirements internal to the organisation, what other strategic goals should a Data Security Management system address?",
        "options": [
            "Regulatory requirements for privacy and confidentiality AND Privacy and Confidentiality needs of all stakeholders",
            "Compliance with ISO29100 and PCI-DSS.",
            "Compliance with ISO27001 and HIPPA",
            "Ensuring the organisation doesn't engage in SPAM marketing"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of these statements best defines Data Security Management?",
        "options": [
            "None of these",
            "The planning, implementation, and testing of security technologies, authentication mechanisms, and other controls to prevent access to information.",
            "The implementation and execution of checkpoints, checklists, controls, and technical mechanisms to govern the access to information in an enterprise",
            "The definition of controls, technical standards, frameworks, and audit trail capabilities to identify who has or has had access to information",
            "The planning, development, and execution of security policies and procedures to provide proper authentication, authorization, access, and auditing of data and information assets"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Preparation and operational activities associated with data interchange include",
        "options": [
            "Operation",
            "Specification and design of operational process",
            "Design, build, and test of dataset creation",
            "Specification for dataset creation",
            "All of the above"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Critical data interchanges are involved in",
        "options": [
            "GIS datasets published to support safety checks before operational digging",
            "Business specific information published to the organization web pages",
            "Issue of contracts and ITTs for bidding",
            "RRP submissions to a regulator",
            "All of the above"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Discovering and documenting metadata about physical data assets provides",
        "options": [
            "An estimation of balance sheet value of enterprise data",
            "Insights into the temporal data quality.",
            "Information on how data is transformed as it moves between systems",
            "Scoping boundaries of the data dictionary",
            "Effective project scope management"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "One of the difficulties when integrating multiple source systems is?",
        "options": [
            "Determining valid links or equivalences between data elements",
            "Completing the Data Architecture on time for the first release",
            "Maintaining documentation describing the data warehouse operation",
            "Having a Data Quality rule applicable to al source systems",
            "Modifying the source systems to align to the enterprise data model."
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "We need to ensure that all data interchange scenarios are managed securely to ensure we?",
        "options": [
            "Have created hash totals on data sets to be exchanged",
            "Have backed up data regularly",
            "Are monitoring the activities of our employees",
            "Are using the most up to date technology",
            "Comply with legal and regulatory or external obligations to publish data"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "In Data Integration, the goal of data discovery is to",
        "options": [
            "Assign data glossary terms and data formats",
            "Identify potential sources and perform a high-level assessment of Data Quality",
            "Assign data glossary terms and canonical models",
            "Identify potential sources and assure data recovery processes are compliant",
            "identify key users and perform a high-level assessment of Data Quality"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the correct definition for change data capture?",
        "options": [
            "A Data Integration approach that updates a Data Warehouse with small changes from Operational Systems",
            "A Data Integration approach that updates the Data Warehouse with big changes from Operational Systems",
            "A Data Warehousing approach to transforming Operational Systems into Data Marts",
            "A Data Quality Initiative that assesses any discrepancies between data stored in a Data Warehouse and data in Operational Systems",
            "A Metadata document that describes how data is transformed in the Data Warehouse"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What is NOT part of Data Integration and Interoperability?",
        "options": [
            "Enterprise Application Integration",
            "Data Quality monitoring",
            "Integrating structured and unstructured data",
            "Archiving data",
            "Data consolidation into hubs or marts"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the advantage of using point-to-point interaction model instead of a hub-and-spoke model?",
        "options": [
            "Management of the number of interfaces is easier",
            "Significant reduction of the complexity of Data Interoperability",
            "The data is automatically sent to the subscribers",
            "Lower latency",
            "Improved data lineage"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of the following are primary deliverables of proper document and record management?",
        "options": [
            "Data from tracking devices, building sensor data.",
            "Managed records in many media formats, e-discovery records, policies and procedures, contracts and financial documents",
            "Spreadsheets, company library books, sales transactions",
            "Local drives of laptops, transcripts of phone calls",
            "Relational databases, database logs, paper documents"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A document management system is an application used to track and store electronic documents and electronic images of paper documents which provides the following capabilities:",
        "options": [
            "Scanning and transcoding of documents",
            "Local disk storage and indexing of documents",
            "Wiki, collaboration, online editing.",
            "Storage, versioning, security, meta-data management, indexing and retrieval",
            "Securing forwarding of documents to colleagues, never having to dispose of documents"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of these describes activities in the document/record management lifecycle?",
        "options": [
            "Identification, management of policies, classification, retention, storage, retrieval and circulation, preservation and disposal",
            "Acquisition, editing, storage, printing, backup, disposal.",
            "Storage, disposal, managing access",
            "Acquisition, classification, storage, purging",
            "Encryption, backup, disposal, extraction"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Non value-added information is often not removed because",
        "options": [
            "Legislation is unclear on what should be kept",
            "Data is an asset. It is likely to be recognized as valuable in the future",
            "The policies are unclear of what is defined as non-value-added, storage is cheap so there is no cost driver, and it takes more effort to dispose than to keep.",
            "We might need the information at a later stage",
            "It should not be removed. All data is value-added"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Documents and records should be classified based on the _______ level of confidentiality for information found in the record.",
        "options": [
            "Average",
            "Highest",
            "Overall",
            "Consensus",
            "General."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which statement best describes the relationship between documents and records?",
        "options": [
            "Documents and records are the same thing",
            "Records are a sub-set of documents",
            "Documents are written and records are audio",
            "Documents and records are not related.",
            "Documents are a sub-set of records"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is not a step in the 'document and content management lifecycle'?",
        "options": [
            "Manage retention and disposal.",
            "Manage versions and control",
            "Capture records and content",
            "Create a content strategy",
            "Audit documents and records"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "For countries, is there an internationally recognized set of codes to use?",
        "options": [
            "Yes, ISO 3166 is the internationally standardized set of codes used by most organizations",
            "No, you should use whatever your organization wants to use",
            "Yes, the standards set are the codes used by your country's postal service",
            "No, organizations should develop their own set of codes to use because the data is used internally",
            "No, there is no internationally recognized set of codes because each country wants to develop their own."
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "As part of the reference Data Stewardship process, it is helpful to capture basic data about each reference data set. Which answer best describes which data should be captured?",
        "options": [
            "Steward name, originating organization, expected frequency of updates, and processes using the reference data",
            "Enterprise Architecture, programming logic, workflows, and ETL relating to any reference data",
            "Metrics to quantify reference data's value to the organization.",
            "Maturity models that access the organization's readiness to accept Data Governance",
            "The names of everyone who is a business or technical user of the reference data"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "A strong argument for pursuing a Reference Data and/or Master Data management initiative is",
        "options": [
            "It will not require a lot of time or effort",
            "They are essential functions in the Data Management Framework",
            "By centralizing the management of reference and master data, the organization can conform critical data needed for analysis",
            "Job security for the data people",
            "It will not require a lot of time"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Are the ISO (International Standards Organization) codes for countries and languages interchangeable?",
        "options": [
            "No, the two codes were developed independently and there was no attempt to use the same code for language as for a country",
            "Yes, the two codes were developed together so that organizations would only have to worry about one set of codes",
            "Yes, the codes can be interchanged unless more than one language is the \"official\"€ language of a country",
            "No because one uses four digits and one uses five digits for the code.",
            "No, because there are more languages than countries"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a primary Master Data Management area of focus?",
        "options": [
            "Generating a golden record / best version of the truth",
            "Producing read-only versions of key data items",
            "Identifying duplicate records",
            "Producing clear data definitions for master data",
            "Providing access to golden data records"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Is the data model important in establishing Master Data Management?",
        "options": [
            "Only if Master Data Management needs to know the processing steps for all data",
            "Yes, Master Data Management needs consistent logical definitions",
            "No, within a given source, data representing the same entity can be different",
            "No, not if the data model is physically instantiated in multiple platforms",
            "No, not if the organization has complex systems with multiple ways of capturing data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Master data differs from reference data in which following way?",
        "options": [
            "Master data does not require a data steward",
            "Unlike reference data, master data is not usually limited to predefined domain values",
            "Master data do not require business definitions",
            "Master data should be held to a higher Data Quality standard than reference data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The \"consumer\" of master data content received from a Master Data Management platform can also be referred to as a",
        "options": [
            "Single version of the truth",
            "Master Data Management platform",
            "Metadata repository",
            "System of record",
            "Subscriber"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "At any given point, master data values should represent what?",
        "options": [
            "The organizations best understanding of everything in the data repository",
            "The organizations best understanding of its conceptual entities",
            "The organizations best understanding of what is accurate and current",
            "The organizations best understanding of the enterprise data model",
            "The organizations best understanding of its transaction data"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Which of these is a valid definition of reference data?",
        "options": [
            "Data used to classify or categorize other data",
            "Data that is fixed and never changes",
            "Data that has a common and widely understood data definition",
            "Data that provides metadata about other data entities",
            "Data that is widely accessed and referenced across an organization"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "When assessing tool to implement master data management solutions, functionality must include",
        "options": [
            "Auto-normalization features",
            "Advanced analytics capabilities",
            "Document and content management",
            "Backup and recovery utilities",
            "Sophisticated integration capability"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which one of the following statements is true?",
        "options": [
            "Reference Data Management involves identifying the 'best' or 'golden' record for each domain.",
            "Master Data Management involves identifying and maintaining approved coded values",
            "Business data stewards maintain lists of valid data values for master data instances.",
            "Master Data Management requires techniques for splitting or merging an instance of a business entity.",
            "Managing reference data requires the same activities and techniques as does managing master data."
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of the following is not a good example of BI?",
        "options": [
            "Statutory reporting to a Regulatory Body",
            "Strategic Analytics for Business Decisions",
            "Decision Support Systems",
            "Supporting Risk Management Decision Reporting",
            "Trend Analysis."
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "When performing an evaluation of analytic applications, which of the following questions is least relevant to identify the level of effort needed?",
        "options": [
            "How much of the tool infrastructure meets our organisational infrastructure",
            "The Standard source systems for which ETL is supplied",
            "Annual costs such as license, maintenance, etc. .",
            "Number of source systems we need to integrate into the tool",
            "How much do the canned processes in the tool match our business"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Slice, Dice, Roll-up and Pivot are terms used in what kind of data processing?",
        "options": [
            "EIEIO",
            "OLTP",
            "ODS",
            "OLAP",
            "EDI"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A comparatively new architectural approach is where volatile data is provisioned in a data warehouse structure to provide transactional systems with a combination of historical and near real time data to meet customer needs. This is a definition of:",
        "options": [
            "Operational Data Store",
            "Active Data Warehousing",
            "Behavioural Decision Support Systems",
            "On Line Analytical Processing Cube",
            "On Line Transactional Processing System"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is a typical metric in data warehouse/BI projects?",
        "options": [
            "Number of indexes used in the fact table",
            "Number of snowflake dimensions used in the projects.",
            "Number of fact tables connected",
            "Number of concurrent users connected to the data warehouse",
            "Number of different metadata used"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT an activity that would enable business acceptance and user satisfaction?",
        "options": [
            "Furnishing and end-to-end verifiable data lineage",
            "Promoting scheduled meetings with user representatives",
            "Understanding the data and defining the operations team's responsiveness to identified issues",
            "Ensuring perceptions of the quality of the data in the BI system are managed",
            "Defining different types of reporting tools to be used for future business needs"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "During the implementation of a data warehouse, a roadmap is used to",
        "options": [
            "Demonstrate progress towards the desired end state",
            "Construct intricate security authorization",
            "Demonstrate alignment to the project plan",
            "Articulate user requirements",
            "Articulate Data Quality checkpoints"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What factors should you consider when choosing data warehouse tools?",
        "options": [
            "Build vs. buy vs. rent",
            "All of the above",
            "Current and future requirements",
            "Current and future costs",
            "Professional service offerings"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The data dictionary describes",
        "options": [
            "Mainly availability and integrity quality rules",
            "Mainly source, target, and transformation rules",
            "Mainly data in XML, JSON, and text forms",
            "Mainly data in business terms directly from the logical model",
            "Mainly extract, transform, and access processes"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "One of the key differences between operational systems and data warehouses is",
        "options": [
            "Operational systems focus on current data; data warehouses contain historical data",
            "Operational systems focus on historical data; data warehouses contain current data",
            "Operational systems focus on Data Quality; data warehouses focus on data security.",
            "Operational systems focus on business processes; data warehouses focus on business strategies",
            "Operational systems are available 24x7; data warehouses are available during business hours"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Updating the Metadata repository is a recommended activity during project close out in the SDLC",
        "options": [
            "FALSE",
            "TRUE"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What type of Metadata provides developers and administrators with knowledge and information about systems?",
        "options": [
            "Unstructured Meta-Data",
            "Technical Operational Meta-Data.",
            "Process Meta-Data",
            "Business Meta-Data",
            "Data Stewardship Meta-Data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "These are examples of which type of Meta-Data: Data Stores & Data Involved, Government/ Regulatory Bodies; Roles & Responsibilities; Process Dependencies and Decomposition:",
        "options": [
            "Data Stewardship Meta-Data",
            "Operational Meta-Data.",
            "Business Meta-Data",
            "Technical Meta-Data",
            "Process Meta-Data"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which of the following is a Metadata scheme focused specifically on documents?",
        "options": [
            "Administrative Meta-Data",
            "Preservation Meta-Data",
            "Structural Meta-Data",
            "Descriptive Meta-Data",
            "Business Meta-Data."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following contain metrics associated with Meta-Data Management?",
        "options": [
            "Steward Representation / Coverage; Meta-Data Repository Availability; Meta-Data Management Maturity",
            "Meta-Data Repository Availability; No. Data Governance Meetings held annually; No. Meta-Data Repositories.",
            "Meta-Data Management Maturity; No. Of Data Stewards; No. Of Meta-Data Attributes Listed",
            "Steward Representation / Coverage; Meta-Data Repository Availability; No. External Reference Data Sources"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Business drivers for managing metadata include the following",
        "options": [
            "Meet data requirements for multiple initiatives and reduce the risk and costs of data integration through the use of consistent reference data.",
            "Strategically prepare organizations to quickly evolve their products, services, and data to take advantage of business opportunities inherent in emerging technologies",
            "Translate business needs into data and system requirements so that processes consistently have the data they require",
            "Reduce data-oriented research time, improve communication between data consumers and IT professionals, and improve time-to-market by reducing system development life-cycle time",
            "Provide a starting point for customization, integration, or even replacement of an application"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "The number of artifacts that must be searched in the metadata repository for all business change projects are",
        "options": [
            "There is no mandatory number of artefacts to be searched but it is highly recommended that the library is examined",
            "Conceptual data models and the business data glossary must be examined",
            "Conceptual, logical, and physical models must be examined",
            "The business data glossary and systems inventory must be consulted.",
            "The business data glossary and data dictionary must be examined"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "By setting, enforcing, and auditing metadata standards, organizations hope to",
        "options": [
            "Ensure the appropriate classification or meta-metadata",
            "Provide activities for the Data Governance office",
            "Standardize business rules in operational processes.",
            "Simplify integration and enable use",
            "Ease of understanding data dictionaries"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Where is the best place to find the following metadata: database table names, column names, and indexes?",
        "options": [
            "Enterprise data model",
            "Logical data model",
            "Database catalog",
            "Security access authorization.",
            "Detailed business processes"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "What is the difference between an industry and a consensus meta-data standard?",
        "options": [
            "Industry standards refer to internationally approved global standards such as ISO whereas consensus standards refer to those agreed to within an organization",
            "The terms are used interchangeably to describe the same concept.",
            "Consensus standards are formed by an international panel of experts whereas industry standards are dictated by a panel of vendors",
            "Industry standards are determined by regulators within a given global region and consensus standards are agreed on by the Data Governance Council within an organization"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The ISO metadata registry standard that provides a framework for defining a metadata registry is",
        "options": [
            "ISO MD 1",
            "ISO 4-20-99",
            "ISO 4590",
            "ISO / IEC 11179",
            "ISO 9001"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Data provenance and data lineage are examples of",
        "options": [
            "Business metadata",
            "Technical metadata",
            "Industry metadata",
            "Operational metadata",
            "Strategic metadata"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Data Quality rules and standards are a form of data. To be effective, they need to be managed as data and rules should be ___________?",
        "options": [
            "Managed outside of the repository and only the results of Data Quality assessments stored as rules metadata",
            "Organized with metrics so the data stewards can review the data and see what rules apply",
            "Focused on rules that can be integrated into application services.",
            "Documented consistently, tied to business impact, backed by data analysis, and assessable to all data consumers",
            "Focused on managing relationships that have gone wrong in the past and may go wrong in the future"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A Data Quality Dimension is",
        "options": [
            "The value of a particular piece of data",
            "A core concept in dimensional modelling",
            "A measurable feature or characteristic of data",
            "A valid value in a list",
            "One aspect of Data Quality used extensively in Data Governance"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The Data Quality Management cycle has four stages. Three are Plan, Monitor, and Act. What is the fourth stage?",
        "options": [
            "Improve",
            "Deploy",
            "Prepare",
            "Reiterate",
            "Manage"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of these is NOT a primary deliverable of Data Quality Management?",
        "options": [
            "Data attribute definitions",
            "Data Quality reports",
            "Data Quality strategy and framework",
            "Analysis from data profiling",
            "Data Quality service level agreements"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a stage of the Data Quality Management Cycle?",
        "options": [
            "Plan",
            "Check",
            "Act",
            "Intervene",
            "Do"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of these is NOT a typical activity in Data Quality Management?",
        "options": [
            "Enterprise Data Modelling",
            "Defining business requirements and business rules",
            "Analysing Data Quality",
            "Creating inspection and monitoring processes",
            "Identifying data problems and issues"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a stage in the Shewhart - Deming Cycle that drives the Data Quality Improvement Lifecycle?",
        "options": [
            "Plan",
            "Investigate",
            "Do",
            "Act",
            "Check"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of these statements is true?",
        "options": [
            "Data Quality Management is the application of technology to data problems",
            "Data Quality Management only addresses structured data",
            "Data Quality Management is usually a one-off project",
            "Data Quality Management is a synonym for Data Governance",
            "Data Quality Management is a continuous process"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What is the goal of collecting and documenting business rules?",
        "options": [
            "To identify potential sources of data for the Data Integration effort",
            "To identify the requirements for the Data Quality",
            "To reuse existing Data Integration solutions",
            "To direct when to manually trigger events and alerts",
            "To design user-experience"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "When defining Data Quality indicators, care must be taken to ensure that they have what?",
        "options": [
            "Measurability, Relevance, and Acceptability",
            "Timeliness, Validity, and Accuracy",
            "A direct link to the Data Governance strategy",
            "Items in the dashboard showing their improvement over time",
            "The core dimensions of Data Quality"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "You are facilitating a committee that is developing data quality metrics. Some of the committee members think that SMART (Specific, Measurable, Accountable, Results-focused, Time-Bound) is a good model. Select the statement that best describes why business relevance needs to be considered as a characteristic of Data Quality Metrics",
        "options": [
            "Unless you use business terms the end-users won't understand and lose interest in the program",
            "Business relevance needs to be considered as a Data Quality metric in its own right",
            "Any IT Program must have some business relevance defined, or it is a waste of time",
            "The value of the metric is limited unless it can be linked to some aspect of a business. The metric's acceptability threshold needs to correlate with business expectations",
            "Expressing business relevance in requirements assists the metadata strategy"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Data for big data ingestion can also be called the data lake. This needs to be carefully managed or the data lake will become?",
        "options": [
            "An organizational statistic",
            "A data swamp.",
            "A biased report",
            "A level of data not usable by data scientists",
            "A data model"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following uses for a Data Mining tool is not optimal?",
        "options": [
            "Identification of data quality issues with your SAP Financial system",
            "Analyse supermarket scanner data to determine when people are most likely to shop and buy certain products",
            "Fraud Detection",
            "Customer Segmentation and Scoring.",
            "Predictive Analysis"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "You need to discover possible relationships or to show data patterns in an exploratory fashion when you do not necessarily have a specific question to ask. What kind of data tool would you use to identify patterns of data using various algorithms?",
        "options": [
            "Data Visualization Application.",
            "Meta-Data Data Lineage View",
            "Data Quality Profiler",
            "Data Mining",
            "ETL Jobs"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A machine learning algorithm that incorrectly classifies new data values may have a problem with population imbalances in",
        "options": [
            "metadata management",
            "big data architecture",
            "model training data",
            "predictive analytics",
            "Reference data management"
        ],
        "correct": 4,
        "explanation": None
    }
]

quiz_data_2 = [
    {
        "question": "What is NOT a discipline of Data Management according to the DAMA DMBOK?",
        "options": [
            "Data Quality Management",
            "Document and Content Management",
            "Data Virtualization",
            "Data Governance",
            "Data Security Management"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The DAMA Wheel contains?",
        "options": [
            "Data Management process",
            "Knowledge areas",
            "Data Management deliverables.",
            "Data Strategy initiatives",
            "Maturity model dimensions"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "How do Data Management professionals maintain commitment of key stakeholders to the Data Management initiative?",
        "options": [
            "Continuous communication, education, and promotion of the importance and value of data and information assets.",
            "Weekly email reports showing metrics on Data Management progress or lack thereof",
            "Rely on the stakeholder group to be self-sustaining",
            "It is not necessary, as the stakeholders signed up at the beginning of the program"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Data standards used by the enterprise must?",
        "options": [
            "Set by a standards organization and not by the enterprise",
            "Be a guideline for the organization but open to the interpretation",
            "Promote consistent results so they are only written once and never updated",
            "Only be necessary for the Data Governance team",
            "Promote consistent results but periodically be reviewed and updated"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Information needs to be managed because",
        "options": [
            "The volumes are large",
            "It is stored in Database systems.",
            "It is an asset of the organization",
            "It contains financial facts"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The Information Lifecycle",
        "options": [
            "Is only important in regulated industries",
            "Is used primarily for Data archiving",
            "Has the same stages as the Systems Delivery Lifecycle",
            "Exists beyond the Systems Delivery Lifecycle",
            "Is not relevant in an Agile environment."
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "When outsourcing information management functions, organisations can",
        "options": [
            "Transfer accountability but not control",
            "Reduce cost of compliance and improve turnaround",
            "Align strategy and control privacy",
            "Improve controls while reducing costs",
            "Transfer control but not accountability."
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What causes data redundancy or data rot?",
        "options": [
            "Dataset inaccuracies developed over time",
            "Server and human error",
            "Poor data management practices",
            "Poor assimilation of collected data",
            "All of the above"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which is the most accurate definition of the term data life cycle?",
        "options": [
            "It represents the theory of data being cross-functional",
            "It represents the path along which data moves from its point of origin to its point of usage, storage, and disposal",
            "It represents managing the risks associated with data",
            "It represents the data used to manage and use data",
            "It represents a range of perspectives on how to approach Data Management"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is not included in the opinion of the European Data Protection Supervisor (EDPS) on data ethics?",
        "options": [
            "Empowered individuals",
            "Accountable controllers who determine personal information processing",
            "Right to request removal of personal data",
            "Privacy-conscious engineering and design of data processing products and services",
            "Future-oriented regulation of data processing and respect for the rights to privacy and to data protection"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "GDPR and PIPEDA are examples of:",
        "options": [
            "primary information parsing algorithms",
            "content management systems",
            "global data modelling standards.",
            "data protection regulations",
            "data program rules"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Data Governance touch points throughout the project lifecycle are facilitated by this organization?",
        "options": [
            "The Project Management Office",
            "The Master Data Office",
            "The Data Governance Office",
            "The Data Stewards Office",
            "The Data Governance Steering Committee."
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "In the Information Management Lifecycle, the Data Governance activity Define the Data Governance Framework is in which Lifecycle stage?",
        "options": [
            "Plan",
            "Specify",
            "Enable",
            "Create and acquire",
            "Maintain and use"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of these is NOT a standard motivation for Data Governance?",
        "options": [
            "Pre-emptive governance",
            "Proactive governance",
            "Devolved Governance.",
            "Reactive governance",
            "Decentralised Governance"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Information Governance and Data Governance should be?",
        "options": [
            "Managed by the Chief Information Office.",
            "Managed as separate functions",
            "Managed as integrated functions, with Data Governance reporting to Information Governance",
            "Managed as a single function",
            "Managed as integrated functions, with Information Governance reporting to Data Governance"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of these does NOT characterize an effective data steward?",
        "options": [
            "Is a recognized subject matter expert in the data subject area / business domain that he/she/they is responsible for",
            "Is a highly experienced technical expert in a variety of data management disciplines & tools.",
            "He/She/They is an effective communicator",
            "He/She/They works collaboratively across the organization with data stakeholders and other identifying data problems and issues",
            "He/She/They works in association with the Data Owner to protect and enhance the data assets under his or her control"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the definition of a business rule in the context of Data Governance?",
        "options": [
            "Contains an organization's contingency plans",
            "Clarifies an organization's goal",
            "Clarifies an organization's objectives",
            "Outlines the steps to take when a business disruption occurs",
            "Defines constraints on what can and cannot be done in the organization"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which framework component of Data Governance includes education, training, and awareness?",
        "options": [
            "Roles",
            "Processes",
            "Tools",
            "Communication",
            "Data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A document that stipulates the responsibilities and acceptable use of data to be exchanged, is commonly referred to as a",
        "options": [
            "Data Sharing Agreement",
            "Data model",
            "Project Charter",
            "Interface Contract",
            "Data Quality Assessment"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What position is responsible for the quality and use of their organization's data assets?",
        "options": [
            "Data Architect",
            "Data Steward",
            "Data Modeler",
            "Data Scientist",
            "Chief Information Officer"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A ______ is used for detailing collaboration principles, escalation, and dispute resolution process between Master Data Management and its data suppliers",
        "options": [
            "Operational level agreement",
            "Warranty",
            "Business requirements document",
            "Operations run book",
            "Metadata catalog"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What position should be responsible for leading the Data Governance Council (DGC)?",
        "options": [
            "Chief Data Architect or Chief Data Modeler",
            "DGC Chair should rotate among executive positions",
            "Chief Data Steward or Chief Data Officer",
            "Any executive can chair the DGC",
            "Chief Information Officer or Chief Technology Officer"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The goal of Data Architecture is to be?",
        "options": [
            "A bridge between business analysis and data modelling",
            "A bridge between technology strategy and database design",
            "A bridge between business strategy and technology execution",
            "A bridge between business execution and technology strategy",
            "A bridge too far."
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "A Data Architecture team is best described as?",
        "options": [
            "An operational data provisioning group",
            "A group of strong database administrators",
            "A well-managed project of architectural development",
            "A strategic planning and compliance team.",
            "The authors of reference data"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "The necessity of representing organizational data at different levels of abstraction is?",
        "options": [
            "Because most organizations have more data than individual people can comprehend, understand, and make decisions about",
            "Because most Chief Data Officers don't have the technical background to be held accountable for complex data diagrams.",
            "Because most organizations need to accommodate the different points of view of information Architecture and Data Architecture",
            "Because most architectures want to deploy a complete suite of drawings for project deliverables",
            "Because most database administrators need specifications to build databases with appropriate response times"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "A CRUD matrix helps organisations map responsibilities for data changes in the business process work flow. CRUD stands for",
        "options": [
            "Cost, Revenue, Uplift, Depreciate",
            "Create, Read, Update, Delete",
            "Create, Review, Use, Destroy",
            "Confidential, Restricted, Unclassified, Destroy",
            "Create, React, Utilise, Delegate."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "The repeated implementation of different CRM Technologies with different data structures is mostly a failure of",
        "options": [
            "Data Warehousing",
            "Data Architecture",
            "Data Quality",
            "Data Security",
            "Data modelling"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the purpose of the Conceptual Data Model?",
        "options": [
            "To define the structure of data elements and to set relationships between them",
            "To provide an experimental perspective of the organization by documenting how different business entities relate to each other",
            "Documents how data are to be stored and accessed on storage media of computer hardware",
            "To provide an outlook of the organization by documenting how different business entities relate to one another",
            "To provide a data-centric perspective of the organization by documenting how different business entities relate to one another"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Data architects create metadata artifacts that constitute valuable ______.",
        "options": [
            "Support for entire organization or enterprise",
            "Database that contain metadata",
            "Business requirements",
            "Opportunities for new marketing offerings",
            "Support for user interfaces"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Components of logical data models include",
        "options": [
            "Attributes.",
            "Entities",
            "Relationships",
            "Keys",
            "All of the above"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What is the difference between cardinality rules and data integrity rules?",
        "options": [
            "Referential integrity rules define the quantity of each entity instance that can participate in a relationship between two entities, and cardinality rules ensure valid values.",
            "Cardinality rules define the quantity of each entity instance that can participate in a relationship between two entities, and referential integrity rules ensure valid values",
            "Referential integrity rules only appear on a relational data model, and cardinality rules only appear on a dimensional data model",
            "There is no difference. Cardinality rules and Referential integrity rules are synonyms",
            "Referential integrity rules quantify the relationships between two or more entities, and cardinality rules quantify the common attributes across entities"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the definition of cardinality?",
        "options": [
            "Count of data tables in a system",
            "Measurement specifications for elements in a dataset",
            "Qualitative description of the relationship of elements across datasets",
            "Defines how many instances of one entity are related to instances of another entity",
            "Classifies variables within a dataset"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "All of the following are properties of a logical data model except",
        "options": [
            "contains attributes",
            "technology-independent",
            "contains relationship cardinality",
            "technology dependent",
            "contains primary keys"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT true of a super-type or sub-type entity relationship?",
        "options": [
            "The subtype relationships should have a discriminator attribute",
            "A sub-type inherits all attributes and relationships of the super-type",
            "Sub-type entities must be mutually exclusive",
            "Attributes and relationships shared by some, but not all, sub-types are modelled with the sub-types",
            "Attributes and relationships shared by all sub-types are modelled with the super-type"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Star and Snowflake are concepts of which Data Modelling Scheme?",
        "options": [
            "Dimensional",
            "Object-oriented",
            "Time-based",
            "NoSQL.",
            "Fact-based"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a Data Modelling style?",
        "options": [
            "CRUD",
            "ORM",
            "UML",
            "IDEF1X",
            "CHEN"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What is the purpose of the Logical Data Model?",
        "options": [
            "To define data elements",
            "To compare data elements",
            "To provide a data-centric perspective of the organization by documenting how business entities relate to one another",
            "To define the structure of data elements and to set relationships between them",
            "To document how data should be stored and accessed"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a key?",
        "options": [
            "Foreign key",
            "Logical Key",
            "Surrogate Key",
            "Primary Key",
            "Alternate Key"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "In the relational data model, what is the best synonym for a \"relation\"?",
        "options": [
            "Association",
            "Tuple",
            "Table",
            "Relationship",
            "Row"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "What are relationship labels in database technology?",
        "options": [
            "Verb phrases describing relationships between data tables",
            "Verb phrases linking business rules with technical specifications",
            "Verb phrases comparing business rules",
            "Verb phrases describing how to take action on the organization's mission statement",
            "Verb phrases describing business rules in each direction between two entities"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Complete the following statement: A business rule ______",
        "options": [
            "Defines an Entity",
            "Defines constraints on what can and cannot be done",
            "Only exists at the level of the physical data model",
            "Identifies an entity instance",
            "Measures a business process"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A database uses foreign keys from code tables for column values. This is a way of implementing",
        "options": [
            "Master Data",
            "Temporal data",
            "Reference Data",
            "Star schema data",
            "Event data"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "The data operations team assures that data is recoverable by which of the following methods",
        "options": [
            "Defining and executing the data recovery plan",
            "Maintaining a test, development, and production environment",
            "Making sure the disks are checked regularly for write errors",
            "Guaranteeing the applications take proper exports of the data",
            "Analysing database error logs"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "A Content Distribution Network supporting a multi-national website is likely to use",
        "options": [
            "A database backup and restore solution",
            "An extract, transform, and load solution",
            "A records disposal solution",
            "A replication solution",
            "An archiving solution"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Database monitoring tools measure key database metrics, such as",
        "options": [
            "Capacity, design, normalization, and user access",
            "Create, read, normalization, and user access",
            "Capacity, availability, backup instances and Data Quality",
            "Capacity , availability, cache performance, and user statistics",
            "Create, read, update and delete"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "In the BASE vs ACID model for transaction processing, \"E\" is best described by which of these statements",
        "options": [
            "Eventual Data Consistency",
            "End to End data consistency",
            "Eventual Availability of Data as described by the CAP theorem",
            "Business Availability of Secure data ELEMENTS",
            "Extra Validation"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Periodic archiving of transaction data from a production CRM system is critical for",
        "options": [
            "Providing alternate sources for reporting systems",
            "Enabling the distribution of transaction data across the enterprise",
            "Managing deleted customer records",
            "Training junior DBAs",
            "The maintenance of database performance"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What should a business continuity plan include?",
        "options": [
            "Defines unplanned disruptions that may occur",
            "Outlines how a business will continue operating during an unplanned disruption in service",
            "Provides explanation to customers during an unplanned disruption in service",
            "Precedes Business rules",
            "Explains to external stakeholders why performance expectations are not being met"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Database performance depends upon two independent facets. These are",
        "options": [
            "Distance to data centre and network bandwidth",
            "Availability and speed",
            "Number of users and number of tables",
            "Hardware and network",
            "Choice of DBMS and programming language"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What is the technique for log-based change of data capturing?",
        "options": [
            "The source system populates specific data elements in the target system",
            "Compare the current state of the source systems to a previous copy",
            "Source Database Management system create data activity logs which are monitored and applied on the target database",
            "The source system processes add to a simple list of changed objects and identifiers on data update",
            "The source system processes copy data that has changed into separate objects as part of the source data update"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Which of the following define the data security touch points in an organisation?",
        "options": [
            "Business rules and process workflow",
            "Risk Assessment",
            "Legislation",
            "Internal Audit",
            "Industry standards."
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Data Security policies should be developed and communicated to ensure that ______?",
        "options": [
            "it is easier to comply that not to comply",
            "External consultants can be used effectively in implementation",
            "Standards and templates can be reused from other organizations",
            "Data that is not Requested, Orchestrated, Technology supported.",
            "External regulatory reviews and audits can be conducted efficiently"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "A security mechanism that searches for customer bank account details in outgoing emails is achieving the goal of",
        "options": [
            "ensuring stakeholder requirements for service and design and experience are met",
            "ensuring stakeholder requirements for concise definitions are usage are met",
            "ensuring stakeholder requirements for confidentiality and privacy are met",
            "ensuring stakeholder requirements for openness and transparency are met"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "In data security, which of the following is not one of the four \"A's\"?",
        "options": [
            "Access",
            "Audit",
            "Authentication",
            "Available",
            "Analyse"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Legislation and Regulation for information security usually focusses on the ______ and not the ______?",
        "options": [
            "Organization/Data",
            "End/Means",
            "Technology/Data",
            "Data/Technology",
            "Executives/Employees"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "An effective Data Security Strategy needs to consider ______ as well as technical security.",
        "options": [
            "Physical (devices, hard copy)",
            "Operational (function, flexibility)",
            "Functional (timing, structures)",
            "Conceptual (metadata, Business Glossary)"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What is the benefit of using role groups to implement Data Security policies?",
        "options": [
            "It allows for iterative reporting of user access",
            "It simplifies revoking individual permissions from an Individual user",
            "It allows users to by typecast by the administrator",
            "It reduces the amount of effort to assign access rights to users if they inherit rights from their group"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "The implementation and administration of Data Security policies is primarily the responsibility of",
        "options": [
            "Knowledge Workers",
            "Security administrators",
            "All staff",
            "The CIO",
            "The CDO"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Obfuscation of data is to",
        "options": [
            "Make it obscure or unclear",
            "Put it in different databases",
            "Use synonyms for the same term",
            "Collect data from obscure sources",
            "Make the results clear"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The percentage of enterprise computers having the most recent security patch installed is a metric of which knowledge area",
        "options": [
            "Data Quality",
            "Data Security",
            "Data Storage and Operations",
            "Metadata Management",
            "Data Warehousing and Business Intelligence"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "HTTPS indicates that the website is",
        "options": [
            "Equipped with a security layer",
            "Equipped with a foreign language translated",
            "Equipped with a content management system",
            "Equipped with third party cookies",
            "Equipped with an underlying database"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The acronym ETL most commonly stands for",
        "options": [
            "Extend Trim Load",
            "Extract Transpose Leverage",
            "Export Transform Log",
            "Extract Transform Load",
            "Efficient Trace Logging"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "When Integrating two data stores using batch or real-time synchronous approaches, results in a difference in",
        "options": [
            "latency",
            "Data Quality",
            "lethargy",
            "source of truth",
            "time stamping"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "An example of an incoming formatted dataset is",
        "options": [
            "Outgoing content examples could be a report, a document, GIS dataset, drawings, models, photographs, records, etc",
            "Specified data extract sent and received within the organization",
            "Data sent and received within an organization",
            "Content formatted for external send e.g. into excel tables as a formatted file",
            "Received content formatted e.g. into excel tables as a formatted file"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What kind of interface is in place when systems are tightly coupled?",
        "options": [
            "A legacy interface",
            "A user interface",
            "An independent interface",
            "A batch interface",
            "A synchronous interface"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which integration approach has a higher latency than event-driven?",
        "options": [
            "Application interface",
            "Batch data integration",
            "Real-time synchronous across systems",
            "Webservices",
            "Streaming access to data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Data sent and received between people or systems within an organization e.g. a report, a document, GIS dataset, drawings, models, photographs, or records is an example of",
        "options": [
            "Internal data interchange",
            "External incoming data interchange",
            "External outgoing data interchange",
            "Regulatory data interchange",
            "All of the above"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Implementing a Services-Oriented Architecture (SOA) will often use",
        "options": [
            "A Data Modelling tool",
            "ETL Servers",
            "A data lake",
            "An enterprise service bus",
            "Data Visualization tools"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "What is NOT an example of an external outgoing data interchange?",
        "options": [
            "Purchased prebuilt data",
            "Outgoing formatted dataset",
            "Outgoing data extract",
            "Response to external request",
            "Outgoing content or document"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What is one of the benefits of Service-Oriented Architecture (SOA)?",
        "options": [
            "Provides an optimized user experience for the data consumer",
            "Allows access to the underlying data structures",
            "Enables application independence and the ability to replace systems without significant changes to interfacing systems",
            "Is the fastest way to develop a new interface",
            "Provides oversight and control to the integration development lifecycle"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "In 2009, ARMA International published GARP for managing records and information. GARP stands for",
        "options": [
            "G20 Approved Recordkeeping Principles",
            "Generally Acceptable Recordkeeping Principles",
            "Generally Available Recordkeeping Practices",
            "Gregarious Archive of Recordkeeping Processes",
            "Global Accredited Recordkeeping Principles."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A goal of 'Document and Content Management' is to ensure effective and efficient retrieval and use of",
        "options": [
            "Information, but not data in unstructured formats",
            "Data and information in unstructured formats",
            "Data and information in structured formats",
            "Data and information in relational formats.",
            "Data, but not information in unstructured formats"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Ontology is the study of",
        "options": [
            "Existence",
            "Beginning",
            "Being and existence",
            "Reality",
            "Knowledge"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "An Enterprise Content Management systems (ECM) stores the following",
        "options": [
            "Code and scripts for enterprise development environments",
            "Documents and images, but not multimedia",
            "Kanban boards",
            "Backups of the enterprise's data warehouse",
            "Information to be displayed on websites and contained in documents"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Which of the following is a reason why organizations do not dispose of non-value-adding information?",
        "options": [
            "The organization's Data Quality benchmark diminishes",
            "Data Modelling the content is difficult to reproduce",
            "Storage is cheap and easily expanded",
            "The information is never out of date",
            "The metadata repository cannot be updated"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "XML provides a language for representing both structured and unstructured data and information",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Users continue to use a shared drive instead of a new Document Management System",
        "options": [
            "Onerous classification requirements when adding documents",
            "A failure to back up the shared drive",
            "Concern about the ability to version documents",
            "Concurrent updates to the document are handled better by the shared drive",
            "The document management system is too expensive"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which one of the following statements is true?",
        "options": [
            "Business data stewards maintain lists of valid data values for master data initiatives",
            "Master Data Management requires techniques for splitting and merging an instance of a business entity",
            "Managing reference data requires the same activities and techniques as does managing master data",
            "Reference Data Management involves identifying the \"best\" or \"golden\" record for each domain",
            "Master Data Management involves identifying and maintaining approved coded values"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "According to the DMBOK, the system that contains the \"best version\" of the master data is the",
        "options": [
            "Spoke",
            "Golden record",
            "Source system",
            "System of record",
            "Consuming system"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A dataset comprised of X, Y coordinates of company stores would be an example of",
        "options": [
            "Metadata",
            "Master Data",
            "Historical Data",
            "Reference Data",
            "Temporary Data"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Plant equipment is an example of",
        "options": [
            "Inverted Data",
            "Transaction Data",
            "None of these",
            "Reference Data",
            "Master Data"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Reference Data",
        "options": [
            "When incorrect has a greater impact that errors in master and transaction data",
            "Is always supplied by outside vendors",
            "Has limited value",
            "Has obvious definitions",
            "Is used to categorize and classify other data"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "What is a common motivation for Reference and Master Data Management?",
        "options": [
            "The need to improve Data Quality and data integrity across multiple data sources",
            "Business Intelligence and data warehousing",
            "The need to build a data dictionary of all the core data entities and attributes",
            "Regulatory acts such as BCBS239, GDPR, and SOX",
            "The need to consolidate all data into one physical database"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Master and reference data are forms of",
        "options": [
            "Data Modeling",
            "Data Quality",
            "Data Security",
            "Data Integration",
            "Data Architecture"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A common driver for initiating a Reference Data Management program is",
        "options": [
            "It fosters the creative use of data",
            "It will improve Data Quality and facilitate analysis across the organization",
            "It can be a one-time-only project",
            "Managing codes and descriptions requires little effort and low cost",
            "It will consolidate the process of securing third party code sets"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT a way of storing Master Data?",
        "options": [
            "Repository",
            "Transaction Hub",
            "Registry",
            "Virtual",
            "Consolidated"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Why would an organization choose to purchase Reference Data?",
        "options": [
            "To set up data compliance and governance processes",
            "To summarize basic information about their enterprise data",
            "To enhance data quality and to facilitate analysis across the organization",
            "To document transactional data systems",
            "To define how data will be captured and tracked"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "When assessing tool to implement Master Data Management solutions, functionality must include",
        "options": [
            "Advanced analytics capabilities",
            "Document and Content management",
            "Backup and recovery utilities",
            "Sophisticated integration capability",
            "Auto-normalization features"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Emergency contact phone number should be found in which master data management program?",
        "options": [
            "Asset",
            "Product",
            "Service",
            "Location",
            "Employee"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Data required across business process, areas and systems is called",
        "options": [
            "Reference and Master",
            "A data mart",
            "Data static",
            "Data Event",
            "Important Data"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Critical to the incremental development of the data warehouse is",
        "options": [
            "A strong release management process",
            "A strong incident management process",
            "The assurance to include velocity, variety, and veracity measurements.",
            "A strong capacity management process",
            "An agile development team"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "A data integration approach that updates a data warehouse with small changes from operational systems is called",
        "options": [
            "ELT",
            "ETL",
            "CDC",
            "EII",
            "SOA"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Which of these is a common OLAP operation?",
        "options": [
            "Roll up",
            "Drill up and drill down",
            "Pivot",
            "Slice and dice",
            "All of the above."
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "The main part of a data vault that houses and integrates data from various source systems is referred to as",
        "options": [
            "Metrics mart",
            "Raw data vault.",
            "Business data vault",
            "Information mart",
            "Persistent staging area"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which users in an organization are more likely to be the recipients of business performance management reporting?",
        "options": [
            "BI team members",
            "Data scientists",
            "Operations",
            "Executives",
            "IT team"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "In its broadest context, the data warehouse includes",
        "options": [
            "Data stores and extracts that can be transformed into star schemas.",
            "All the data in the enterprise",
            "Either an Inmon or Kimball approach",
            "Any data stores or extracts used to support the delivery for BI purposes",
            "An integrated data store, ETL logic, and extensive data cleansing routines"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Dimension tables",
        "options": [
            "Are the same as Facts",
            "Have many columns but few rows",
            "Have few columns but many rows",
            "Contain measures.",
            "Do not contain hierarchies"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "What technique will identify the system of record for the data?",
        "options": [
            "Data profiling",
            "Collection of business rules",
            "Definition of Data Integration and Lifecycle requirements",
            "data discovery",
            "Analysis of lineage"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "According to Henry Morris of IDC, Analytical Applications provide business with a pre-built solution to optimize a functional area or industry vertical",
        "options": [
            "FALSE",
            "TRUE"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "We would expect to consult the Metadata Library when",
        "options": [
            "Selecting a Data Storage device",
            "Implementing a Data Quality tool",
            "Formulating a Governance policy",
            "Accessing the internet.",
            "Assessing the impact of change"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "To which of the following initiatives was the establishment of an industry Metadata Standard essential?",
        "options": [
            "Internet Protocols",
            "EDI",
            "BASEL II/SOX.",
            "Proprietary XML",
            "JSON"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "We do not expect to consult the Metadata repository when",
        "options": [
            "Undertaking a data quality assessment",
            "None of these.",
            "Investigating a data issue",
            "Updating the operating system that the Master Data management toolset is running on",
            "Assessing the impact of change"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "The Metadata repository enables us to establish multiple perspectives of data. These are:",
        "options": [
            "Business and Technical Perspective",
            "3rd normal form and un normalised",
            "Dimensional and non dimensional perspective.",
            "Structured and Unstructured",
            "Internal and External"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What would you not expect to find in the Metadata repository?",
        "options": [
            "Data Lineage diagrams and models",
            "Data storage devices",
            "Data Dictionary.",
            "Data Requirements",
            "Data Models"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "A business perspective product in the Metadata repository is",
        "options": [
            "Data Glossary",
            "ETL flow",
            "Systems Inventory",
            "Data Dictionary",
            "Physical Data Model"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "The library of information about our data (our metadata) is built so that",
        "options": [
            "All of these.",
            "We can have a shared formalized view of requirements (e.g. what data quality we need)",
            "We can better understand it",
            "We can be consistent in our use of terminology",
            "We can better manage it"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Which of these statements are true about Metadata?",
        "options": [
            "The repository is always a hybrid architecture.",
            "A Metadata repository and a Glossary are synonyms",
            "The repository is always a centralized architecture",
            "The repository is always a decentralized architecture",
            "Data models are components of a Metadata repository"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "A data lineage tool enables a user to",
        "options": [
            "Enables rapid development of dashboard reporting",
            "Track the data from source system to a target database; understanding its transformations.",
            "Visualize how the data gets to the data lake",
            "Track the historical changes to a data value",
            "Line up the data to support sophisticated glossary management"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A 'Data Swamp' is a data lake that has become",
        "options": [
            "overly catalogued, holding information and data",
            "suitable for frogs, toads and salamanders",
            "modelled, managed and muddy",
            "a data asset that uses machine learning.",
            "messy, unclean and inconsistent"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "An umbrella term for any classification or controlled vocabulary is",
        "options": [
            "Data model",
            "Taxonomy",
            "Metadata",
            "Dictionary",
            "English."
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Metadata repository processes will not include",
        "options": [
            "Managing change to data products (e.g. data dictionary or business data glossary) entries. For example: new data terms to be defined, new data requirements, adding new database tables, or including new systems into the technical landscape",
            "Assessing impact where a change to existing data product entries are proposed e.g. the impact of change on related data on other systems",
            "Selecting Data Management library software, search, and storage technologies",
            "Controlling versions of a data product that will be required to manage the required single published master copy in conjunction with the variants potentially established as work in progress"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Top-down and Bottom-up data analysis and profiling are best done in concert because",
        "options": [
            "It gives something for the architects to do while the profiles get on with the work",
            "It gets everyone involved",
            "It balances business relevance and the actual state of the data",
            "It allows the profilers to show the business the true state of the data",
            "Data Quality tools are more productive when they are effectively configured"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Which of these is NOT an expected role of a Data Quality Oversight Board?",
        "options": [
            "Data Profiling and Analysis",
            "Setting Data Quality Improvement priorities",
            "Establishing communications and feedback mechanisms",
            "Development and maintaining Data Quality",
            "Producing certification and compliance policies"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "According to the DMBOK, which of these is NOT a valid dimension of Data Quality?",
        "options": [
            "Currency",
            "Timeliness",
            "Reasonableness",
            "Relevance",
            "Completeness"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "What is the purpose of a data lineage tool?",
        "options": [
            "List of potential data integration opportunities",
            "Tracking Historical changes to a dataset",
            "Formal Data Quality Assessment of a dataset",
            "Description of a dataset's phase within the data lifecycle",
            "Collection of all the metadata related to a dataset"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Which of the following is NOT usually a feature of Data Quality improvement tools?",
        "options": [
            "Transformation",
            "Standardization",
            "Parsing",
            "Data profiling",
            "Data Modelling"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "A Data Quality Service Level Agreement (SLA) would normally include which of these",
        "options": [
            "A breakdown of the costs of Data Quality improvement",
            "Roles and responsibilities for Data Quality",
            "A business case for data improvement",
            "An enterprise data model",
            "Detailed technical specifications for data transfer"
        ],
        "correct": 1,
        "explanation": None
    },
    {
        "question": "Data quality measurements can be taken at three levels of granularity. They are:",
        "options": [
            "Fine data, coarse data, and rough data",
            "Person data, location data, and product data",
            "Departmental data, regional data, and enterprise data",
            "Data element value, data instance or record, and data set",
            "Historical data, current data, and future dated data"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "When the DMBOK calls Data Quality Management a program, not a project, it means",
        "options": [
            "Data Quality has both project and maintenance work along with communications and training",
            "Data Quality is more tightly scoped and planned than ordinary projects",
            "Data Quality practices can stop at the end of the project",
            "Data Quality managers can be paid more that project managers",
            "Data quality management is really expensive"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "Whose responsibility should it be to identify and report occurrences of defects in information and data?",
        "options": [
            "Any employee",
            "The information quality team",
            "Customers",
            "The IT department",
            "Regulatory compliance officers"
        ],
        "correct": 0,
        "explanation": None
    },
    {
        "question": "What is manual directed Data Quality correction?",
        "options": [
            "Using a Data Quality improvement manual to guide data cleanse and correction activities",
            "The automation of all data cleanse and correction routines",
            "The use of automated cleanse and correction tools with results manually checked before committing outputs",
            "The use of spreadsheets to manually inspect and correct data",
            "Teams of data creators supervised by data subject matter experts"
        ],
        "correct": 2,
        "explanation": None
    },
    {
        "question": "Which one of these is a key process in defining Data Quality business rules?",
        "options": [
            "Matching data from different data sources",
            "Producing Data Quality reports and dashboards",
            "Producing Data Management policies",
            "De-duplicating data records",
            "Separating data that does not meet business needs from data that does"
        ],
        "correct": 4,
        "explanation": None
    },
    {
        "question": "Big data is often defined by three characteristics. They are:",
        "options": [
            "Size, Speed, and Sensitivity",
            "Complexity, Compliance and Completeness",
            "Expansive, Engaged and Enormous.",
            "Volume, Variety, and Velocity",
            "Direction, Depth and Details"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "Big data management requires",
        "options": [
            "a certification in data science",
            "no discipline at all",
            "big ideas with big budgets.",
            "more discipline than relational data management",
            "less discipline than relational data management"
        ],
        "correct": 3,
        "explanation": None
    },
    {
        "question": "A 'Data Lake' is an environment where a vast amount of data can be",
        "options": [
            "ingested, screened, obfuscated and purged",
            "digested, processed, deleted and visualised",
            "updated, obfuscated, nullified and cleansed",
            "ingested, shared, assessed and analysed",
            "purged, sorted, split and scanned"
        ],
        "correct": 3,
        "explanation": None
    },
    

]

# Header
st.sidebar.markdown('''
- [Quiz 1: CDMP Data Management Exam Revision COMPLETE Course](#quiz-1-cdmp-data-management-exam-revision-complete-course)
''')

st.header("Quiz 1: CDMP Data Management Exam Revision COMPLETE Course")
st.write(str(len(quiz_data_1)) + ' questions')
st.markdown("---")

# Display all questions
for i, question_data in enumerate(quiz_data_1):
    st.subheader(f"Question {i+1}")
    st.write(question_data["question"])
    
    # Create a unique key for each question's radio buttons
    radio_key = f"1_question_{i}"
        
    # Radio buttons with callback
    selected_option = st.radio(
        "Select your answer:",
        options=question_data["options"],
        index=None,
        key = radio_key)
    if selected_option is not None:
        selected_index = question_data["options"].index(selected_option)
    
    # Show feedback if an answer is selected
    if selected_option:
        if selected_index == question_data["correct"]:
            st.success("Correct! ✓")
        else:
            st.error("Incorrect ✗")
        
        # Show explanation
        if question_data['explanation'] is not None:
            st.info(f"Explanation: {question_data['explanation']}")
    
    st.markdown("---")





# Header
st.sidebar.markdown('''
- [Quiz 2: CDMP Data Management Exam Revision COMPLETE Course](#quiz-2-cdmp-data-management-exam-revision-complete-course)
''')

st.header("Quiz 2: CDMP Data Management Exam Revision COMPLETE Course")
st.write(str(len(quiz_data_2)) + ' questions')
st.markdown("---")

# Display all questions
for i, question_data in enumerate(quiz_data_2):
    st.subheader(f"Question {i+1}")
    st.write(question_data["question"])
    
    # Create a unique key for each question's radio buttons
    radio_key = f"2_question_{i}"
        
    # Radio buttons with callback
    selected_option = st.radio(
        "Select your answer:",
        options=question_data["options"],
        index=None,
        key = radio_key)
    if selected_option is not None:
        selected_index = question_data["options"].index(selected_option)
    
    # Show feedback if an answer is selected
    if selected_option:
        if selected_index == question_data["correct"]:
            st.success("Correct! ✓")
        else:
            st.error("Incorrect ✗")
        
        # Show explanation
        if question_data['explanation'] is not None:
            st.info(f"Explanation: {question_data['explanation']}")
    
    st.markdown("---")





import random

# 1. Combine all questions into one list
all_questions = quiz_data_1 + quiz_data_2

st.sidebar.markdown('''
- [Random Practice Mode](#random-practice-mode)
''')
st.header("Random Practice Mode")

# 2. Create a 'slot' in memory to hold the random question
if "random_q" not in st.session_state:
    st.session_state.random_q = None

# 3. The "Generate" button
if st.button("Get a Random Question"):
    st.session_state.random_q = random.choice(all_questions)

# 4. Display the question (Same format as your original code)
if st.session_state.random_q:
    q = st.session_state.random_q
    st.subheader("Practice Question")
    st.write(q["question"])
    
    # We use the question text itself as a 'key' 
    # This trick makes sure the radio button resets when a new question is generated
    selected_option = st.radio(
        "Select your answer:",
        options=q["options"],
        index=None,
        key=f"random_{q['question']}" 
    )
    
    if selected_option:
        selected_index = q["options"].index(selected_option)
        if selected_index == q["correct"]:
            st.success("Correct! ✓")
        else:
            st.error("Incorrect ✗")
            # st.info(f"The correct answer is: {q['options'][q['correct']]}")



