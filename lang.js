// js/lang.js

const translations = {
  pt: {
    // Hero
    "hero-badge": "Oncologista Clínico",
    "hero-subtitle": "Informações sobre câncer para pacientes e familiares, além de conteúdo em pesquisa e bioestatística para profissionais de saúde.",
    "hero-cta-phone": "Ligar agora",
    "hero-cta-book": "Agendar consulta",

    // Features section
    "features-label": "Conteúdo",
    "features-title": "O que você encontra aqui",
    "features-subtitle": "Recursos para pacientes, familiares e profissionais de saúde",

    // Card descriptions
    "card-general-desc": "Conteúdo acessível para pacientes e familiares sobre prevenção, mitos e informações gerais sobre o câncer.",
    "card-tumors-desc": "Informações detalhadas sobre os principais tipos de câncer, com linguagem acessível e embasamento científico.",
    "card-research-desc": "Conteúdo em bioestatística e pesquisa clínica para profissionais de saúde, mestrandos e doutorandos.",

    // About section labels
    "about-label": "Currículo",

    // Contact section labels
    "contact-label": "Contato",
    "contact-subtitle": "Envie uma mensagem ou agende diretamente pelo WhatsApp",

    // Navbar
    "nav-home": "Início",
    "nav-curriculo": "Currículo",
    "nav-depoimentos": "Depoimentos",
    "nav-contatos": "Contatos",
    "nav-socials": "Redes Sociais",
    "nav-onc-calcs": "Onc Calcs",
    "nav-search": "Buscar...",

    // Onc Calcs dropdown
    "calc-clearance": "Clearance de Creatinina",
    "calc-bsa": "Superfície Corpórea",
    "calc-carbodose": "Dose de Carboplatina",
    "calc-psakinetics": "Cinética PSA",

    // Carousel captions
    "carousel-slide1-caption": "Informações para pacientes, familiares, médicos e pesquisadores.",
    "carousel-slide2-title": "Vacinas",
    "carousel-slide2-p": "Pacientes com câncer podem se <a href=\"https://youtu.be/nh1ZhnJ_GDE\" class=\"text-primary\"><span style=\"text-decoration:underline\">vacinar</span></a>?",
    "carousel-slide3-title": "Câncer de pele",
    "carousel-slide3-p": "Qual especialista <a href=\"https://youtu.be/eR0U5e4rKOk\"><span class=\"text-primary\" style=\"text-decoration:underline\">procurar</span></a>?",

    // Cards
    "card-general-title": "Temas em Geral",
    "card-general-link-vaccines": "Vacinas e câncer",
    "card-general-link-exercise": "Atividade física e câncer",
    "card-general-link-myths": "Mitos sobre câncer",
    "card-more": "Mais...",

    "card-tumors-title": "Tipos de tumores",
    "card-tumors-link-colorectal": "Câncer Colorretal",
    "card-tumors-link-breast": "Câncer de Mama",
    "card-tumors-link-lung": "Câncer de Pulmão",

    "card-research-title": "Pesquisa e Biostat",
    "card-research-link-intro": "Introdução Bioestatística",
    "card-research-link-spss": "SPSS Kaplan Meier",
    "card-research-link-endnote": "EndNote importando estilo",

    // About section
    "about-title": "Sobre Dr. Allan Pereira",
    "about-subtitle": "Saiba mais sobre o autor do Site",

    // Tabs
    "tab-career": "Formação e carreira",
    "tab-awards": "Prêmios e Awards",
    "tab-media": "Na mídia",

    // Career bullet points
    "career-1": "Oncologista clínico titular do Hospital Sírio-Libanês.",
    "career-2": "Chefe do Serviço de Oncologia do Hospital de Base do DF.",
    "career-3": "Pós-doutorado na Universidade do Texas - M.D. Anderson Cancer Center (Houston, Tx, EUA).",
    "career-4": "Doutorado no programa de oncologia pela Universidade de São Paulo (USP).",
    "career-5": "Oncologista Clínico formado pelo Hospital Sírio-Libanês (São Paulo).",
    "career-6": "Título de especialista em Oncologia Clínica pela Sociedade Brasileira de Oncologia Clínica (SBOC).",
    "career-7": "Fez parte do Grupo de Tumores Gastrointestinais e do Grupo de Câncer de Mama do Instituto do Câncer do Estado de São Paulo (ICESP/FM USP).",
    "career-8": "É autor de publicações em periódicos internacionais e capítulos de livros em temas diversos da oncologia.",
    "career-9": "Membro da European Society for Medical Oncology (ESMO), da American Society of Clinical Oncology (ASCO) e da American Association for Cancer Research (AACR).",
    "career-10": "Graduação em medicina pela Universidade Federal do Rio Grande do Norte - UFRN (2007).",
    "career-11": "Título de Residência Médica em Clínica Médica pela Irmandade Santa Casa de Misericórdia de São Paulo - ISCMSP (2010).",
    "career-12": "Credenciado pelo Educational Commission of Foreign Medical Graduates (ECFMG) / United States Medical Licensing Examination (USMLE).",

    // Media tab video titles
    "media-video-1": "Apresentação - Hospital Sírio-Libanês",
    "media-video-2": "Alô Enfermeiro - Hospital de Base do DF",
    "media-video-3": "COVID-19 Orientações Pacientes SUS",
    "media-video-4": "Novidades ASCO - 2019",
    "media-video-5": "Julho Verde",

    // Footer
    "footer-offices-title": "Consultórios",
    "footer-offices-cta": "Clique para detalhes:",
    "footer-unit1": "Unidade 1",
    "footer-unit2": "Unidade 2",
    "footer-social-title": "Redes Sociais",
    "footer-appointment-title": "Marque uma consulta",
    "footer-message-cta": "Mande uma mensagem.",
    "footer-or-btn": "Ou clique no botão:",
    "footer-book-btn": "Agendar consulta",

    // Modals – General Topics
    "modal-general-title": "Temas em Geral",
    "modal-general-desc": "Este é um conteúdo direcionado a pacientes e familiares, com uso de linguagem mais acessível e com menos termos técnicos, sobre assuntos de interesse comum.",
    "modal-general-link-vaccines": "Vacinas e câncer",
    "modal-general-link-exercise": "Atividade física e câncer",
    "modal-general-link-myths": "Mitos sobre o câncer",
    "modal-general-link-rights": "Direitos do paciente",

    // Modals – Tumor Types
    "modal-tumors-title": "Tipos de Tumores",
    "modal-tumors-desc": "Informações completas com linguagem fácil.",
    "modal-tumors-link-colorectal": "Câncer Colorretal",
    "modal-tumors-link-breast": "Câncer de Mama",
    "modal-tumors-link-lung": "Câncer de Pulmão",
    "modal-tumors-link-hn": "Câncer de Cabeça e Pescoço - Julho Verde",
    "modal-tumors-link-skin": "Cânceres de Pele e Melanoma",

    // Modals – Research
    "modal-research-title": "Pesquisa e Bioestatística",
    "modal-research-desc": "Conteúdo destinado a pesquisadores, alunos de mestrado e doutorado. Aqui teremos discussões de temas relacionados à pesquisa clínica, bem como videoaulas com dicas sobre como conduzir as análises mais comuns.",

    // Shared modal actions
    "modal-close": "Fechar",
    "modal-save-location": "Salvar Local",

    // Contact section
    "contact-title": "Entre em Contato",
    "contact-name-label": "Nome",
    "contact-email-label": "Email",
    "contact-phone-label": "Telefone/Celular",
    "contact-message-label": "Mensagem",
    "contact-name": "Nome",
    "contact-email": "Email",
    "contact-phone": "Telefone/Celular",
    "contact-message": "Digite aqui...",
    "contact-send": "Enviar mensagem"
  },

  en: {
    // Hero
    "hero-badge": "Clinical Oncologist",
    "hero-subtitle": "Cancer information for patients and families, plus research and biostatistics content for healthcare professionals.",
    "hero-cta-phone": "Call now",
    "hero-cta-book": "Book appointment",

    // Features section
    "features-label": "Content",
    "features-title": "What you'll find here",
    "features-subtitle": "Resources for patients, families and healthcare professionals",

    // Card descriptions
    "card-general-desc": "Accessible content for patients and families on prevention, myths and general cancer information.",
    "card-tumors-desc": "Detailed information on the most common cancer types, in plain language with scientific grounding.",
    "card-research-desc": "Biostatistics and clinical research content for healthcare professionals, master's and PhD students.",

    // About section labels
    "about-label": "CV",

    // Contact section labels
    "contact-label": "Contact",
    "contact-subtitle": "Send a message or book directly via WhatsApp",

    // Navbar
    "nav-home": "Home",
    "nav-curriculo": "CV",
    "nav-depoimentos": "Testimonials",
    "nav-contatos": "Contact",
    "nav-socials": "Social Media",
    "nav-onc-calcs": "Onc Calcs",
    "nav-search": "Search...",

    // Carousel captions
    "carousel-slide1-caption": "Information for patients, families, physicians and researchers.",
    "carousel-slide2-title": "Vaccines",
    "carousel-slide2-p": "Can cancer patients get <a href=\"https://youtu.be/nh1ZhnJ_GDE\" class=\"text-primary\"><span style=\"text-decoration:underline\">vaccinated</span></a>?",
    "carousel-slide3-title": "Skin cancer",
    "carousel-slide3-p": "Which specialist should you <a href=\"https://youtu.be/eR0U5e4rKOk\"><span class=\"text-primary\" style=\"text-decoration:underline\">consult</span></a>?",

    // Onc Calcs dropdown
    "calc-clearance": "Creatinine Clearance",
    "calc-bsa": "Body Surface Area",
    "calc-carbodose": "Carboplatin Dose",
    "calc-psakinetics": "PSA Kinetics",

    // Cards
    "card-general-title": "General Topics",
    "card-general-link-vaccines": "Vaccines and cancer",
    "card-general-link-exercise": "Exercise and cancer",
    "card-general-link-myths": "Cancer myths",
    "card-more": "More...",

    "card-tumors-title": "Tumor types",
    "card-tumors-link-colorectal": "Colorectal Cancer",
    "card-tumors-link-breast": "Breast Cancer",
    "card-tumors-link-lung": "Lung Cancer",

    "card-research-title": "Research & Biostat",
    "card-research-link-intro": "Introduction to Biostatistics",
    "card-research-link-spss": "SPSS Kaplan-Meier",
    "card-research-link-endnote": "EndNote importing styles",

    // About section
    "about-title": "About Dr. Allan Pereira",
    "about-subtitle": "Learn more about the author of this website",

    // Tabs
    "tab-career": "Training and Career",
    "tab-awards": "Awards and Honors",
    "tab-media": "In the media",

    // Career bullet points
    "career-1": "Clinical Oncologist at Hospital Sírio-Libanês.",
    "career-2": "Head of Oncology at Hospital de Base do Distrito Federal.",
    "career-3": "Post-doctoral fellowship at The University of Texas MD Anderson Cancer Center (Houston, TX, USA).",
    "career-4": "PhD in Oncology, University of São Paulo (USP).",
    "career-5": "Clinical Oncology residency at Hospital Sírio-Libanês (São Paulo).",
    "career-6": "Board-certified in Clinical Oncology by the Brazilian Society of Clinical Oncology (SBOC).",
    "career-7": "Member of the Gastrointestinal Tumor and Breast Cancer Groups at Instituto do Câncer do Estado de São Paulo (ICESP/FM USP).",
    "career-8": "Author of publications in international journals and book chapters on various oncology topics.",
    "career-9": "Member of the European Society for Medical Oncology (ESMO), the American Society of Clinical Oncology (ASCO), and the American Association for Cancer Research (AACR).",
    "career-10": "Medical degree from Universidade Federal do Rio Grande do Norte – UFRN (2007).",
    "career-11": "Internal Medicine residency at Irmandade Santa Casa de Misericórdia de São Paulo – ISCMSP (2010).",
    "career-12": "Certified by the Educational Commission for Foreign Medical Graduates (ECFMG) / United States Medical Licensing Examination (USMLE).",

    // Media tab video titles
    "media-video-1": "Introduction – Hospital Sírio-Libanês",
    "media-video-2": "Healthcare Q&A – Hospital de Base do DF",
    "media-video-3": "COVID-19 Guidance for SUS Patients",
    "media-video-4": "ASCO Updates – 2019",
    "media-video-5": "July Green (Head & Neck Cancer Awareness)",

    // Footer
    "footer-offices-title": "Offices",
    "footer-offices-cta": "Click for details:",
    "footer-unit1": "Unit 1",
    "footer-unit2": "Unit 2",
    "footer-social-title": "Social Media",
    "footer-appointment-title": "Book an Appointment",
    "footer-message-cta": "Send a message.",
    "footer-or-btn": "Or click the button:",
    "footer-book-btn": "Book appointment",

    // Modals – General Topics
    "modal-general-title": "General Topics",
    "modal-general-desc": "Content directed at patients and families, using accessible language with fewer technical terms on topics of common interest.",
    "modal-general-link-vaccines": "Vaccines and cancer",
    "modal-general-link-exercise": "Exercise and cancer",
    "modal-general-link-myths": "Cancer myths",
    "modal-general-link-rights": "Patient rights",

    // Modals – Tumor Types
    "modal-tumors-title": "Tumor Types",
    "modal-tumors-desc": "Complete information in accessible language.",
    "modal-tumors-link-colorectal": "Colorectal Cancer",
    "modal-tumors-link-breast": "Breast Cancer",
    "modal-tumors-link-lung": "Lung Cancer",
    "modal-tumors-link-hn": "Head and Neck Cancer – July Green",
    "modal-tumors-link-skin": "Skin Cancers and Melanoma",

    // Modals – Research
    "modal-research-title": "Research and Biostatistics",
    "modal-research-desc": "Content for researchers, master's and doctoral students. Topics cover clinical research methodology and video tutorials on the most common statistical analyses.",

    // Shared modal actions
    "modal-close": "Close",
    "modal-save-location": "Save Location",

    // Contact section
    "contact-title": "Get in Touch",
    "contact-name-label": "Name",
    "contact-email-label": "Email",
    "contact-phone-label": "Phone",
    "contact-message-label": "Message",
    "contact-name": "Name",
    "contact-email": "Email",
    "contact-phone": "Phone",
    "contact-message": "Type your message here...",
    "contact-send": "Send"
  }
};

function applyLanguage(lang) {
  // Ajusta atributo lang do <html>
  document.documentElement.lang = (lang === "pt") ? "pt-BR" : "en";

  // Textos com data-i18n
  document.querySelectorAll("[data-i18n]").forEach(function (el) {
    const key = el.getAttribute("data-i18n");
    const value = translations[lang] && translations[lang][key];
    if (value) {
      el.textContent = value;
    }
  });

  // Elements needing innerHTML (text with embedded links)
  document.querySelectorAll("[data-i18n-html]").forEach(function (el) {
    const key = el.getAttribute("data-i18n-html");
    const value = translations[lang] && translations[lang][key];
    if (value) {
      el.innerHTML = value;
    }
  });

  // Placeholders (inputs, textarea etc)
  document.querySelectorAll("[data-i18n-placeholder]").forEach(function (el) {
    const key = el.getAttribute("data-i18n-placeholder");
    const value = translations[lang] && translations[lang][key];
    if (value) {
      el.setAttribute("placeholder", value);
    }
  });

  // Salva preferência no navegador
  if (window.localStorage) {
    localStorage.setItem("site-lang", lang);
  }
}

function initLanguageSwitcher() {
  const btnPt = document.getElementById("btn-pt");
  const btnEn = document.getElementById("btn-en");

  if (btnPt) {
    btnPt.addEventListener("click", function () {
      applyLanguage("pt");
    });
  }

  if (btnEn) {
    btnEn.addEventListener("click", function () {
      applyLanguage("en");
    });
  }

  // Língua inicial: tenta carregar do localStorage, senão pt
  let lang = "pt";
  if (window.localStorage) {
    const stored = localStorage.getItem("site-lang");
    if (stored === "pt" || stored === "en") {
      lang = stored;
    }
  }
  applyLanguage(lang);
}

// Garante que só rode depois do DOM estar pronto
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initLanguageSwitcher);
} else {
  initLanguageSwitcher();
}
