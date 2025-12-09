from flask import Flask, render_template, url_for

app = Flask(__name__)

CURSOS = [
    {
        "id": 1,
        "nome": "Programação em Java",
        "descricao_curta": "Curso completo de Java para iniciantes.",
        "descricao_longa": """
Este curso de Programação em Java foi desenvolvido para levar o aluno do nível iniciante ao nível intermediário, oferecendo uma base sólida na linguagem mais utilizada no mundo corporativo. O aluno começa entendendo os princípios fundamentais da programação e evolui gradualmente até dominar conceitos essenciais para aplicações modernas.

O curso aborda:
• Fundamentos da linguagem Java: sintaxe, tipos de dados, variáveis e operadores.  
• Estruturas de controle: if, else, switch, loops e boas práticas de uso.  
• Programação orientada a objetos (POO): classes, objetos, herança, polimorfismo e encapsulamento.  
• Manipulação de arrays, listas, coleções e estruturas de dados mais comuns.  
• Tratamento de exceções, erros e criação de códigos robustos.  
• Introdução a APIs, pacotes, bibliotecas e modularização de projetos.  
• Criação de pequenos sistemas e aplicações reais para reforçar o aprendizado.  

Ao final do curso, o aluno estará apto a criar programas bem estruturados, entender projetos existentes e avançar para áreas como desenvolvimento web, mobile (Android) ou back-end corporativo com frameworks como Spring.
""",
        "carga": "45 horas"
    },
    {
        "id": 2,
        "nome": "Design Gráfico",
        "descricao_curta": "Criação de artes profissionais.",
        "descricao_longa": """
Este curso oferece uma formação completa em Design Gráfico, combinando teoria, prática e ferramentas profissionais usadas no mercado. Ele é ideal para quem deseja trabalhar com criação visual, edição de imagens, artes para redes sociais e projetos gráficos em geral.

Conteúdo abordado:
• Fundamentos do design: cores, contrastes, tipografia, espaçamento e hierarquia visual.  
• Composição e princípios de layout para projetos digitais e impressos.  
• Edição de imagens profissional utilizando ferramentas como Photoshop e Illustrator.  
• Criação de banners, posts, logotipos, cartões de visita e materiais institucionais.  
• Técnicas de manipulação, tratamento e retoque fotográfico.  
• Montagem de conteúdo para redes sociais e identidade visual.  
• Exportação, padronização e qualidade final para arquivos digitais e impressos.  

Ao final do curso, o aluno será capaz de criar artes profissionais, desenvolver identidades visuais completas e atuar em agências, marketing digital ou como freelancer.
""",
        "carga": "40 horas"
    },
    {
        "id": 3,
        "nome": "Marketing Digital",
        "descricao_curta": "Domine estratégias modernas de vendas.",
        "descricao_longa": """
Este curso de Marketing Digital prepara o aluno para dominar as estratégias utilizadas pelas maiores empresas, agências e profissionais do setor. Ele cobre desde os fundamentos até técnicas avançadas usadas para atrair clientes, vender mais e construir presença online.

Conteúdos estudados:
• Introdução ao marketing moderno e comportamento do consumidor digital.  
• SEO (otimização para mecanismos de busca): ranqueamento, palavras-chave e autoridade.  
• Tráfego Pago: Facebook Ads, Instagram Ads, Google Ads e estratégias de segmentação.  
• Copywriting: como escrever textos persuasivos para anúncios, páginas e campanhas.  
• Estratégias de funis de vendas, remarketing e automações inteligentes.  
• Gestão de conteúdo e redes sociais com foco em crescimento orgânico.  
• Análise de métricas e tomada de decisão baseada em dados (Google Analytics, Meta Ads).  

No final do curso, o aluno terá capacidade para criar campanhas profissionais, analisar resultados, otimizar anúncios e atuar como gestor de tráfego, social media ou estrategista digital.
""",
        "carga": "50 horas"
    }
]

@app.route("/")
def index():
    return render_template("index.html", cursos=CURSOS)

@app.route("/curso/<int:id>")
def curso(id):
    curso_encontrado = next((c for c in CURSOS if c["id"] == id), None)
    return render_template("curso.html", curso=curso_encontrado)

@app.route("/contato")
def contato():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
