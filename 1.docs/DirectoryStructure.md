```text
event-horizon/
├── 1.docs/
│   ├── 1.Requirements/
│   │   └── RequirementDefinition.md
│   ├── 2.BasicDesign/
│   │   └── ERD.svg
│   ├── 3.DetailedDesign/
│   │   ├── API_design.md
│   │   ├── GeneratedSchema.sql
│   │   └── Schema.dbml
│   ├── 4.Architecture/
│   ├── 5.Testing/
│   ├── 6.UserManual/
│   ├── 7.MeetingNotes/
│   │   └── 2025-06-18_meeting_notes.md
│   └── DirectoryStructure.md
├── 2.infra/
│   ├── aws/
│   │   ├── cloudwatch/
│   │   ├── codepipeline/
│   │   │   └── buildspec.yml
│   │   ├── ec2/
│   │   │   └── user-data.sh
│   │   └── secrets/
│   │       └── env.example
│   ├── ngnix/
│   │   └── nginx.conf
│   └── docker-compose.prod.yml
├── 3.frontend/
├── 4.backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── .env
│   └── requirements.txt
├── 5.tools/
│   └── generate_tree.py
├── .gitignore
├── LICENSE
├── README.md
└── docker-compose.yml
```
