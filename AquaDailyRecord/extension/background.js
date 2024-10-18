chrome.runtime.onInstalled.addListener(() => {
  console.log("AquaDailyRecord 背景腳本已啟動");
});

// chrome.runtime.onInstalled.addListener(({ reason }) => {
//   if (reason === "install") {
//     chrome.tabs.create({
//       url: "index.html",
//     });
//   }
// });
