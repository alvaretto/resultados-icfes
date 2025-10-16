#!/bin/bash
# Script para hacer push a GitHub con manejo de credenciales
# Institución Educativa Pedacito de Cielo

echo "================================================================================"
echo "  🚀 PUSH A GITHUB PARA STREAMLIT CLOUD"
echo "  Institución Educativa Pedacito de Cielo"
echo "================================================================================"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Verificar que estamos en el directorio correcto
if [ ! -d ".git" ]; then
    print_error "No estás en un repositorio Git"
    exit 1
fi

# Verificar si hay commits pendientes
UNPUSHED=$(git log origin/main..HEAD --oneline 2>/dev/null | wc -l)
if [ $UNPUSHED -eq 0 ]; then
    print_success "No hay commits pendientes de push"
    echo ""
    print_info "Tu repositorio ya está actualizado en GitHub"
    exit 0
fi

print_warning "Hay $UNPUSHED commit(s) pendiente(s) de push"
echo ""

# Mostrar commits pendientes
echo "Commits pendientes:"
git log origin/main..HEAD --oneline
echo ""

# Preguntar método de autenticación
echo "================================================================================"
echo "  🔐 MÉTODO DE AUTENTICACIÓN"
echo "================================================================================"
echo ""
echo "Elige un método para hacer push:"
echo ""
echo "1) Token de Acceso Personal (Recomendado)"
echo "   - Más seguro"
echo "   - Fácil de revocar"
echo "   - No expira la sesión"
echo ""
echo "2) Limpiar credenciales y volver a autenticar"
echo "   - Útil si tienes credenciales incorrectas"
echo ""
echo "3) Usar SSH (requiere configuración previa)"
echo "   - Más seguro a largo plazo"
echo "   - Requiere clave SSH configurada"
echo ""
echo "4) Intentar push normal (puede fallar si hay problemas de credenciales)"
echo ""
read -p "Selecciona una opción (1-4): " OPCION

case $OPCION in
    1)
        echo ""
        echo "================================================================================"
        echo "  📝 PUSH CON TOKEN DE ACCESO PERSONAL"
        echo "================================================================================"
        echo ""
        print_info "Si no tienes un token, créalo en: https://github.com/settings/tokens"
        print_info "Permisos necesarios: 'repo' (acceso completo a repositorios)"
        echo ""
        read -p "Ingresa tu token de acceso personal: " TOKEN
        
        if [ -z "$TOKEN" ]; then
            print_error "Token vacío. Abortando."
            exit 1
        fi
        
        echo ""
        print_info "Haciendo push con token..."
        
        # Hacer push con token
        git push https://$TOKEN@github.com/alvaretto/resultados-icfes.git main
        
        if [ $? -eq 0 ]; then
            print_success "Push exitoso!"
            echo ""
            read -p "¿Quieres guardar este token para futuros push? (s/n): " GUARDAR
            if [ "$GUARDAR" == "s" ] || [ "$GUARDAR" == "S" ]; then
                git remote set-url origin https://$TOKEN@github.com/alvaretto/resultados-icfes.git
                print_success "Token guardado. Futuros push usarán este token automáticamente."
            fi
        else
            print_error "Push falló. Verifica tu token."
            exit 1
        fi
        ;;
        
    2)
        echo ""
        echo "================================================================================"
        echo "  🔄 LIMPIAR CREDENCIALES"
        echo "================================================================================"
        echo ""
        print_info "Limpiando credenciales almacenadas..."
        
        git credential reject <<EOF
protocol=https
host=github.com
EOF
        
        print_success "Credenciales limpiadas"
        echo ""
        print_info "Ahora intenta hacer push. Te pedirá usuario y token."
        print_info "Username: alvaretto"
        print_info "Password: [tu token de acceso personal]"
        echo ""
        
        git push origin main
        ;;
        
    3)
        echo ""
        echo "================================================================================"
        echo "  🔑 PUSH CON SSH"
        echo "================================================================================"
        echo ""
        
        # Verificar si hay clave SSH
        if [ -f ~/.ssh/id_ed25519.pub ] || [ -f ~/.ssh/id_rsa.pub ]; then
            print_success "Clave SSH encontrada"
            
            # Cambiar remote a SSH
            print_info "Cambiando remote a SSH..."
            git remote set-url origin git@github.com:alvaretto/resultados-icfes.git
            
            print_info "Haciendo push..."
            git push origin main
            
            if [ $? -eq 0 ]; then
                print_success "Push exitoso!"
            else
                print_error "Push falló. Verifica tu configuración SSH."
                print_info "Asegúrate de haber añadido tu clave SSH a GitHub:"
                print_info "https://github.com/settings/keys"
            fi
        else
            print_error "No se encontró clave SSH"
            print_info "Genera una con: ssh-keygen -t ed25519 -C 'tu@email.com'"
            print_info "Luego añádela a GitHub: https://github.com/settings/keys"
            exit 1
        fi
        ;;
        
    4)
        echo ""
        echo "================================================================================"
        echo "  🔄 PUSH NORMAL"
        echo "================================================================================"
        echo ""
        print_info "Intentando push normal..."
        
        git push origin main
        
        if [ $? -eq 0 ]; then
            print_success "Push exitoso!"
        else
            print_error "Push falló"
            print_info "Prueba con la opción 1 (Token) o 2 (Limpiar credenciales)"
        fi
        ;;
        
    *)
        print_error "Opción inválida"
        exit 1
        ;;
esac

# Si llegamos aquí, el push fue exitoso
echo ""
echo "================================================================================"
echo "  ✅ PUSH COMPLETADO"
echo "================================================================================"
echo ""
print_success "Los cambios están ahora en GitHub"
echo ""
print_info "Próximos pasos para Streamlit Cloud:"
echo ""
echo "1. Ir a: https://share.streamlit.io"
echo "2. Acceder a tu aplicación"
echo "3. Verificar Settings → Main file path = 'app_resultados_icfes_completo.py'"
echo "4. Menú (⋮) → Reboot app"
echo "5. Esperar 1-2 minutos"
echo "6. En la app: presionar 'C' para limpiar caché"
echo "7. Refrescar navegador (Ctrl+Shift+R)"
echo ""
print_success "Deberías ver el Modelo Flexible y todas las comparativas"
echo ""
echo "================================================================================"

