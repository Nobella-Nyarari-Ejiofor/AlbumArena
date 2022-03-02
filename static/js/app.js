function copyToClipboard() {
  var copyText = document.getElementById("share-link");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
}