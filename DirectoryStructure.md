Event Horizon/
├── 1.docs/
│   ├── 1.Requirements/
│   │   └── RequirementDefinition.md
│   ├── 2.BasicDesign/
│   │   └── BasicDesign.md
│   ├── 3.DetailedDesign/
│   │   └── DetailedDesign.md
│   ├── 4.Architecture/
│   │   └── DeploymentPlan.md
│   ├── 5.Testing/
│   │   └── TestingPlan.md
│   ├── 6.UserManual/
│   └── 7.Notes/
│
├── 2.infra/
│   ├── aws/
│   │   ├── ec2/
│   │   │   └── user-data.sh
│   │   ├── codepipeline/
│   │   │   └── buildspec.yml
│   │   ├── cloudwatch/
│   │   └── secrets/
│   │       └── env.example
│   ├── nginx/
│   │   └── nginx.conf
│   └── docker-compose.prod.yml
│
├── 3.frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   ├── calendar/
│   │   │   ├── messaging/
│   │   │   └── posts/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Profile.jsx
│   │   │   └── Calendar.jsx
│   │   ├── assets/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── Dockerfile
│   └── package.json
│
├── 4.backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   ├── posts.py
│   │   │   │   ├── events.py
│   │   │   │   └── dms.py
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── post.py
│   │   │   ├── event.py
│   │   │   ├── message.py
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .env
├── .gitignore
├── DirectoryStructure.md
├── docker-compose.yml
├── LICENSE
└── README.md
