/**
 * Script para inspeccionar la estructura de los archivos Excel
 */

import * as XLSX from 'xlsx';
import * as path from 'path';

const EXCEL_FILES = [
  'data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx',
  'data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx',
];

function inspectExcel(filePath: string) {
  console.log(`\n${'='.repeat(80)}`);
  console.log(`📊 Inspeccionando: ${filePath}`);
  console.log('='.repeat(80));

  try {
    const workbook = XLSX.readFile(filePath);
    
    console.log(`\n📄 Hojas disponibles: ${workbook.SheetNames.join(', ')}`);
    
    // Inspeccionar la primera hoja
    const firstSheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[firstSheetName];
    
    // Convertir a JSON para ver la estructura
    const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
    
    console.log(`\n📋 Primeras 10 filas de "${firstSheetName}":`);
    console.log('─'.repeat(80));
    
    data.slice(0, 10).forEach((row: any, index: number) => {
      console.log(`Fila ${index}:`, row);
    });
    
    // Mostrar encabezados
    if (data.length > 0) {
      console.log(`\n📌 Encabezados detectados:`);
      console.log((data[0] as any[]).join(' | '));
    }
    
    // Convertir a JSON con encabezados
    const jsonData = XLSX.utils.sheet_to_json(worksheet);
    console.log(`\n📊 Total de registros: ${jsonData.length}`);
    
    if (jsonData.length > 0) {
      console.log(`\n🔍 Ejemplo de registro (primero):`);
      console.log(JSON.stringify(jsonData[0], null, 2));
    }
    
  } catch (error) {
    console.error(`❌ Error al leer ${filePath}:`, error);
  }
}

// Inspeccionar todos los archivos
EXCEL_FILES.forEach(inspectExcel);

