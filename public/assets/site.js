// Apenas navegação móvel. Sem cookies, armazenamento local ou chamadas externas.
"use strict";
document.documentElement.classList.add("js");
const toggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navigation");
const isEnglish = document.documentElement.lang === "en";
if (toggle && navigation) {
  toggle.hidden = false;
  const close = () => {
    navigation.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "Menu +";
  };
  toggle.addEventListener("click", () => {
    const opened = navigation.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(opened));
    toggle.textContent = opened ? (isEnglish ? "Close −" : "Fechar −") : "Menu +";
  });
  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) close();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navigation.classList.contains("open")) {
      close();
      toggle.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".site-header")) close();
  });
  window.matchMedia("(min-width: 721px)").addEventListener("change", close);
}
