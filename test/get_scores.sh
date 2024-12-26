curl --location --request GET 'http://127.0.0.1:8000/api/scores?model=Unbabel/wmt22-cometkiwi-da' \
--header 'Content-Type: application/json' \
--data '[
    {"src": "How to Demonstrate Your Strategic Thinking Skills", "mt": "Cómo demostrar su capacidad de pensamiento estratégico" },{ "src": "Why is Accuracy important in the workplace?", "mt": "¿Por qué es importante la precisión en el trabajo" }, { "src": "When faced with a large amount of analysis ask for support setting up a team to approach the issue in different ways.", "mt": "Cuando se enfrente a una gran cantidad de análisis, pida ayuda para crear un equipo que aborde la cuestión de diferentes maneras." }
]'
