const $templateInput = document.querySelector("#review-template");

$templateInput.addEventListener("input", (e) => {
  const { value } = e.currentTarget;

  // 使用 chrome.storage 同步設定
  chrome.storage.sync.set({ reviewTemplate: value });
});
