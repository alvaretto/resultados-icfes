# Analisis Resultados ICFES 2025 - I.E. Pedacito de Cielo

App Streamlit para analisis de resultados ICFES Saber 11 (2024-2025). Stack: Python, Streamlit, Pandas, Plotly, Anthropic/Groq APIs.

## Regla de Paralelizacion

Cuando el usuario pida 2+ tareas independientes, SIEMPRE lanzarlas como agentes paralelos en worktrees aislados. Nunca ejecutar secuencialmente lo que puede ir en paralelo.
