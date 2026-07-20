(() => {
  "use strict";

  const MEASUREMENT_ID = "G-7DN1BVZBCJ";
  const STORAGE_KEY = "kgaid.analytics-consent.v1";
  const isPolish = document.documentElement.lang.toLowerCase().startsWith("pl");

  const copy = isPolish
    ? {
        title: "Analityka i prywatność",
        description:
          "Ta strona korzysta z opcjonalnego Google Analytics 4, aby właściciel mógł zobaczyć zbiorcze statystyki odwiedzin. Analityka zostanie włączona dopiero po Twojej zgodzie. Statystyki nie są widoczne publicznie.",
        privacy: "Polityka prywatności Google",
        accept: "Zgadzam się",
        reject: "Odrzucam",
        settings: "Ustawienia prywatności",
      }
    : {
        title: "Analytics and privacy",
        description:
          "This site uses optional Google Analytics 4 so the owner can view aggregate visit statistics. Analytics is enabled only after you consent. The statistics are not public.",
        privacy: "Google Privacy Policy",
        accept: "Accept analytics",
        reject: "Reject analytics",
        settings: "Privacy settings",
      };

  window.dataLayer = window.dataLayer || [];
  window.gtag =
    window.gtag ||
    function gtag() {
      window.dataLayer.push(arguments);
    };

  window.gtag("consent", "default", {
    analytics_storage: "denied",
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    wait_for_update: 500,
  });

  let analyticsLoaded = false;
  let banner;

  function readChoice() {
    try {
      const choice = window.localStorage.getItem(STORAGE_KEY);
      return choice === "granted" || choice === "denied" ? choice : null;
    } catch {
      return null;
    }
  }

  function saveChoice(choice) {
    try {
      window.localStorage.setItem(STORAGE_KEY, choice);
    } catch {
      // The choice remains valid for the current page even when storage is unavailable.
    }
  }

  function clearAnalyticsCookies() {
    const domain = window.location.hostname;
    const parentDomain = domain.includes(".") ? `.${domain}` : domain;

    document.cookie.split(";").forEach((cookie) => {
      const name = cookie.split("=")[0].trim();
      if (!name.startsWith("_ga")) return;

      const expiry = "Thu, 01 Jan 1970 00:00:00 GMT";
      document.cookie = `${name}=; expires=${expiry}; path=/`;
      document.cookie = `${name}=; expires=${expiry}; path=/; domain=${domain}`;
      document.cookie = `${name}=; expires=${expiry}; path=/; domain=${parentDomain}`;
    });
  }

  function loadAnalytics() {
    if (analyticsLoaded) return;
    analyticsLoaded = true;

    window.gtag("consent", "update", {
      analytics_storage: "granted",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
    });
    window.gtag("js", new Date());
    window.gtag("config", MEASUREMENT_ID, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      send_page_view: true,
    });

    const script = document.createElement("script");
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(
      MEASUREMENT_ID,
    )}`;
    script.dataset.kgaidAnalytics = "true";
    document.head.appendChild(script);
  }

  function hideBanner() {
    if (banner) banner.hidden = true;
  }

  function showBanner() {
    if (banner) banner.hidden = false;
  }

  function acceptAnalytics() {
    saveChoice("granted");
    hideBanner();
    loadAnalytics();
  }

  function rejectAnalytics() {
    saveChoice("denied");
    window.gtag("consent", "update", {
      analytics_storage: "denied",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
    });
    clearAnalyticsCookies();
    hideBanner();
  }

  function addStyles() {
    const style = document.createElement("style");
    style.id = "kgaid-consent-styles";
    style.textContent = `
      .kgaid-consent[hidden] { display: none; }
      .kgaid-consent {
        position: fixed;
        z-index: 1000;
        right: 20px;
        bottom: 20px;
        width: min(520px, calc(100vw - 32px));
        padding: 22px;
        border: 1px solid rgba(148, 163, 184, 0.35);
        border-radius: 18px;
        background: #0b1728;
        color: #e5edf7;
        box-shadow: 0 24px 70px rgba(0, 0, 0, 0.42);
        font: inherit;
      }
      .kgaid-consent h2 {
        margin: 0 0 10px;
        color: #ffffff;
        font-size: 1.15rem;
      }
      .kgaid-consent p {
        margin: 0;
        color: #cbd5e1;
        line-height: 1.55;
      }
      .kgaid-consent a {
        color: #8fd3ff;
      }
      .kgaid-consent-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 18px;
      }
      .kgaid-consent button,
      .kgaid-privacy-button {
        border: 1px solid rgba(148, 163, 184, 0.45);
        border-radius: 999px;
        padding: 10px 16px;
        font: inherit;
        font-weight: 700;
        cursor: pointer;
      }
      .kgaid-consent-accept {
        border-color: transparent !important;
        background: #4fd1c5;
        color: #07111f;
      }
      .kgaid-consent-reject {
        background: transparent;
        color: #e5edf7;
      }
      .kgaid-privacy-button {
        padding: 0;
        border: 0;
        border-radius: 0;
        background: transparent;
        color: inherit;
        text-decoration: underline;
        font-weight: inherit;
      }
      .kgaid-consent button:focus-visible,
      .kgaid-privacy-button:focus-visible {
        outline: 3px solid #8fd3ff;
        outline-offset: 3px;
      }
      @media (max-width: 640px) {
        .kgaid-consent {
          right: 16px;
          bottom: 16px;
          padding: 18px;
        }
        .kgaid-consent-actions button {
          flex: 1 1 160px;
        }
      }
    `;
    document.head.appendChild(style);
  }

  function buildInterface() {
    addStyles();

    banner = document.createElement("section");
    banner.className = "kgaid-consent";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-labelledby", "kgaid-consent-title");
    banner.innerHTML = `
      <h2 id="kgaid-consent-title">${copy.title}</h2>
      <p>${copy.description} <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">${copy.privacy}</a>.</p>
      <div class="kgaid-consent-actions">
        <button type="button" class="kgaid-consent-accept">${copy.accept}</button>
        <button type="button" class="kgaid-consent-reject">${copy.reject}</button>
      </div>
    `;
    banner.querySelector(".kgaid-consent-accept").addEventListener("click", acceptAnalytics);
    banner.querySelector(".kgaid-consent-reject").addEventListener("click", rejectAnalytics);
    document.body.appendChild(banner);

    const settingsButton = document.createElement("button");
    settingsButton.type = "button";
    settingsButton.className = "kgaid-privacy-button";
    settingsButton.textContent = copy.settings;
    settingsButton.addEventListener("click", showBanner);

    const footer = document.querySelector(".site-footer .footer-inner");
    if (footer) {
      const wrapper = document.createElement("p");
      wrapper.appendChild(settingsButton);
      footer.appendChild(wrapper);
    } else {
      document.body.appendChild(settingsButton);
    }
  }

  buildInterface();

  const choice = readChoice();
  if (choice === "granted") {
    hideBanner();
    loadAnalytics();
  } else if (choice === "denied") {
    hideBanner();
  } else {
    showBanner();
  }
})();
