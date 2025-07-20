```text
event-horizon/
├── 1.docs/
│   ├── 1.Requirements/
│   │   └── RequirementDefinition.md
│   ├── 2.BasicDesign/
│   │   ├── ERD.svg
│   │   └── ERD_20250721.svg
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
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   │   └── index.ts
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   └── ProtectedRoute.tsx
│   │   │   ├── layout/
│   │   │   └── posts/
│   │   ├── hooks/
│   │   │   └── useAuth.ts
│   │   ├── pages/
│   │   │   ├── FeedPage.tsx
│   │   │   ├── LoginPage.tsx
│   │   │   └── RegisterPage.tsx
│   │   ├── store/
│   │   │   └── authStore.ts
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   ├── .gitignore
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── 4.backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── posts.py
│   │   │   └── users.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── security.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── .env
│   └── requirements.txt
├── 5.tools/
│   └── generate_tree.py
├── .gitignore
├── LICENSE
├── README.md
└── docker-compose.yml
```
