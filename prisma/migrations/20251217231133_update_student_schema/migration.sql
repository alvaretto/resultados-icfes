-- CreateTable
CREATE TABLE "Student" (
    "id" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "primerApellido" TEXT NOT NULL,
    "segundoApellido" TEXT NOT NULL,
    "primerNombre" TEXT NOT NULL,
    "segundoNombre" TEXT NOT NULL,
    "tipoDocumento" TEXT NOT NULL,
    "numeroDocumento" TEXT NOT NULL,
    "grupo" TEXT NOT NULL,
    "modelo" TEXT NOT NULL,
    "anio" INTEGER NOT NULL,
    "lecturaCritica" INTEGER NOT NULL,
    "matematicas" INTEGER NOT NULL,
    "socialesCiudadanas" INTEGER NOT NULL,
    "cienciasNaturales" INTEGER NOT NULL,
    "ingles" INTEGER NOT NULL,
    "puntajeGlobal" INTEGER NOT NULL,

    CONSTRAINT "Student_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "Student_modelo_idx" ON "Student"("modelo");

-- CreateIndex
CREATE INDEX "Student_anio_idx" ON "Student"("anio");

-- CreateIndex
CREATE INDEX "Student_grupo_idx" ON "Student"("grupo");

-- CreateIndex
CREATE UNIQUE INDEX "Student_numeroDocumento_anio_key" ON "Student"("numeroDocumento", "anio");
