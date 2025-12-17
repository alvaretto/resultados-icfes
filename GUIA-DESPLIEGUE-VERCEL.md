# 🚀 Guía de Despliegue en Vercel

## ✅ Requisitos Previos

- ✅ Cuenta de Vercel (gratuita): https://vercel.com/signup
- ✅ Repositorio Git (GitHub, GitLab o Bitbucket)
- ✅ Proyecto Next.js funcionando localmente

---

## 📋 Método 1: Deploy desde CLI (Rápido)

### Paso 1: Instalar Vercel CLI

```bash
npm i -g vercel
```

### Paso 2: Login en Vercel

```bash
vercel login
```

### Paso 3: Deploy (Preview)

```bash
cd /home/bootcamp/Proyectos-2026/icfes-analysis-nextjs
vercel
```

Sigue las preguntas:
- Set up and deploy? **Y**
- Which scope? Selecciona tu cuenta
- Link to existing project? **N**
- What's your project's name? `icfes-analysis`
- In which directory is your code located? `./`
- Want to override settings? **N**

### Paso 4: Deploy a Producción

```bash
vercel --prod
```

---

## 🌐 Método 2: Deploy desde Dashboard (Recomendado)

### Paso 1: Push a GitHub

```bash
cd /home/bootcamp/Proyectos-2026/icfes-analysis-nextjs

# Inicializar git si no está inicializado
git init

# Agregar archivos
git add .
git commit -m "🚀 Initial commit - Clean Architecture"

# Crear repositorio en GitHub y push
git remote add origin https://github.com/TU-USUARIO/icfes-analysis-nextjs.git
git branch -M main
git push -u origin main
```

### Paso 2: Importar en Vercel

1. Ve a https://vercel.com/new
2. Click en "Import Project"
3. Selecciona tu repositorio de GitHub
4. Vercel detectará automáticamente Next.js

### Paso 3: Configurar Variables de Entorno

En el dashboard de Vercel, configura:

```env
# Production Database
POSTGRES_PRISMA_URL="postgresql://..."
POSTGRES_URL_NON_POOLING="postgresql://..."

# Next.js
NEXT_PUBLIC_APP_URL="https://tu-app.vercel.app"
```

### Paso 4: Deploy

Click en "Deploy" - ¡Listo! 🎉

---

## 🗄️ Configurar Vercel Postgres

### Opción A: Desde Dashboard

1. Ve a tu proyecto en Vercel
2. Click en "Storage" tab
3. Click en "Create Database"
4. Selecciona "Postgres"
5. Click en "Continue"
6. Vercel creará la base de datos y las variables de entorno automáticamente

### Opción B: Desde CLI

```bash
vercel env add POSTGRES_PRISMA_URL
vercel env add POSTGRES_URL_NON_POOLING
```

---

## 📊 Migrar Base de Datos

### Paso 1: Actualizar Schema para PostgreSQL

Crear `prisma/schema-prod.prisma`:

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider  = "postgresql"
  url       = env("POSTGRES_PRISMA_URL")
  directUrl = env("POSTGRES_URL_NON_POOLING")
}

// ... resto del schema
```

### Paso 2: Deploy del Schema

```bash
# Desde local con conexión a Vercel Postgres
npx prisma db push

# O usar Vercel CLI
vercel env pull .env.production
npx prisma db push
```

### Paso 3: Seed de Datos (Opcional)

```bash
npx prisma db seed
```

---

## 🔧 Configuración de Build

Vercel detecta automáticamente Next.js, pero puedes personalizar en `vercel.json`:

```json
{
  "buildCommand": "prisma generate && next build",
  "devCommand": "next dev",
  "installCommand": "npm install"
}
```

---

## 🚦 Verificar Deploy

### 1. Check Build Logs

En el dashboard de Vercel, revisa los logs de build para errores.

### 2. Test Preview

Cada PR crea un preview deployment automático:
- URL: `https://icfes-analysis-[hash].vercel.app`

### 3. Test Production

- URL: `https://icfes-analysis.vercel.app`
- Custom domain: `https://tu-dominio.com`

---

## 📈 Monitoring

### Analytics (Incluido)

Vercel incluye analytics automáticamente:
- Visits
- Top Pages
- Top Referrers
- Devices

### Speed Insights (Gratis)

Habilita Speed Insights en Settings:
- Performance metrics
- Core Web Vitals
- Real User Monitoring

---

## 🔄 CI/CD Automático

Una vez conectado a Git:

1. **Push a branch** → Crea preview deployment
2. **Merge a main** → Deploy automático a producción
3. **Rollback** → Un click en el dashboard

---

## 🌍 Custom Domain

### Paso 1: Agregar Dominio

1. Ve a Project Settings → Domains
2. Agrega tu dominio: `tudominio.com`

### Paso 2: Configurar DNS

Vercel te dará los records DNS para configurar:

```
Type  Name  Value
A     @     76.76.21.21
CNAME www   cname.vercel-dns.com
```

### Paso 3: Verificar

Vercel verificará automáticamente y configurará SSL (gratis con Let's Encrypt).

---

## 🔒 Environment Variables

### Development vs Production

```bash
# Local development
.env.local

# Vercel environment variables
Project Settings → Environment Variables
```

### Variables por Environment

- Development
- Preview
- Production

Puedes tener diferentes valores para cada uno.

---

## 📦 Build Cache

Vercel cachea automáticamente:
- `node_modules`
- `.next` build output
- Prisma client

Esto hace que los builds sean **muy rápidos** (típicamente <30s).

---

## 🐛 Troubleshooting

### Build Failed

```bash
# Ver logs completos
vercel logs

# Deploy con logs verbosos
vercel --debug
```

### Database Connection Issues

Verifica variables de entorno:
```bash
vercel env ls
vercel env pull
```

### TypeScript Errors

```bash
# Verificar localmente primero
npm run type-check
npm run build
```

---

## ✅ Checklist de Deploy

- [ ] Código en Git
- [ ] Prisma schema actualizado para PostgreSQL
- [ ] Variables de entorno configuradas
- [ ] Build local exitoso (`npm run build`)
- [ ] Tests pasando
- [ ] Database migrada
- [ ] Deploy a preview funcionando
- [ ] Deploy a producción
- [ ] Custom domain configurado (opcional)
- [ ] Analytics habilitado
- [ ] Monitoring configurado

---

## 🎯 URLs del Proyecto

**Local:**
- http://localhost:3000

**Preview (cada PR):**
- https://icfes-analysis-[hash].vercel.app

**Production:**
- https://icfes-analysis.vercel.app
- https://tu-dominio.com (si configuraste)

---

## 📚 Recursos

- [Vercel Docs](https://vercel.com/docs)
- [Next.js on Vercel](https://vercel.com/docs/frameworks/nextjs)
- [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)
- [Prisma on Vercel](https://www.prisma.io/docs/guides/deployment/deployment-guides/deploying-to-vercel)

---

**Autor:** AI Senior Software Engineer  
**Fecha:** 2025-12-17  
**Versión:** 1.0

