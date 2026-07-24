(function () {
  const SOURCE_LANG = "es";
  const LANGUAGES = {
    es: "Español",
    en: "English",
  };

  const COOKIE_NAME = "googtrans";
  const COOKIE_DAYS = 365;

  function setCookie(name, value) {
    const expires = new Date(Date.now() + COOKIE_DAYS * 864e5).toUTCString();
    const base = `${name}=${value}; expires=${expires}; path=/; SameSite=Lax`;
    document.cookie = base;

    const host = location.hostname;
    if (host && !host.includes("localhost") && !/^\d+\.\d+\.\d+\.\d+$/.test(host)) {
      document.cookie = `${base}; domain=.${host}`;
    }
  }

  function clearCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/`;

    const host = location.hostname;
    if (host && !host.includes("localhost") && !/^\d+\.\d+\.\d+\.\d+$/.test(host)) {
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=.${host}`;
    }
  }

  function getCookie(name) {
    return document.cookie
      .split("; ")
      .find((row) => row.startsWith(`${name}=`))
      ?.split("=")[1];
  }

  function currentLanguage() {
    const cookie = decodeURIComponent(getCookie(COOKIE_NAME) || "");
    if (cookie.endsWith("/en")) return "en";
    return "es";
  }

  function applyLanguage(lang) {
    if (lang === "es") {
      clearCookie(COOKIE_NAME);
      clearCookie(`${COOKIE_NAME}`);
    } else {
      setCookie(COOKIE_NAME, `/${SOURCE_LANG}/${lang}`);
    }

    localStorage.setItem("wikiLanguage", lang);
    location.reload();
  }

  function renderSelector() {
    const topbar = document.querySelector(".topbar");
    if (!topbar || document.querySelector(".language-switcher")) return;

    const activeLang = localStorage.getItem("wikiLanguage") || currentLanguage();
    document.documentElement.lang = activeLang;

    const switcher = document.createElement("div");
    switcher.className = "language-switcher";
    switcher.setAttribute("aria-label", "Elegir idioma");

    Object.entries(LANGUAGES).forEach(([lang, label]) => {
      const button = document.createElement("button");
      button.type = "button";
      button.dataset.lang = lang;
      button.textContent = lang.toUpperCase();
      button.title = label;
      button.setAttribute("aria-label", label);
      button.className = activeLang === lang ? "is-active" : "";
      button.addEventListener("click", () => applyLanguage(lang));
      switcher.appendChild(button);
    });

    const nav = topbar.querySelector(".nav-links");
    topbar.insertBefore(switcher, nav || null);
  }

  window.googleTranslateElementInit = function () {
    new window.google.translate.TranslateElement(
      {
        pageLanguage: SOURCE_LANG,
        includedLanguages: "es,en",
        autoDisplay: false,
        layout: window.google.translate.TranslateElement.InlineLayout.SIMPLE,
      },
      "google_translate_element"
    );
  };

  function loadGoogleTranslate() {
    if (document.querySelector("#google_translate_element")) return;

    const holder = document.createElement("div");
    holder.id = "google_translate_element";
    holder.setAttribute("aria-hidden", "true");
    document.body.appendChild(holder);

    const script = document.createElement("script");
    script.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
    script.async = true;
    document.body.appendChild(script);
  }

  document.addEventListener("DOMContentLoaded", () => {
    renderSelector();
    loadGoogleTranslate();
  });
})();
