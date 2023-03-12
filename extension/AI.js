chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.windows.create({
    "url": "popup.html",
    "type": "popup",
    "width": 300,
    "height": 200
  });
});

document.addEventListener('DOMContentLoaded', function() {
  var saveButton = document.getElementById('save-button');
  var inputField = document.getElementById('input-field');
  var status = document.getElementById('status');

  saveButton.addEventListener('click', function() {
    var textToSave = inputField.value;
    chrome.fileSystem.chooseEntry({ type: 'openDirectory' }, function(directoryEntry) {
      if (chrome.runtime.lastError) {
        status.textContent = 'Error choosing directory: ' + chrome.runtime.lastError.message;
        return;
      }

      var filename = 'extension.txt';
      directoryEntry.getFile(filename, { create: true }, function(fileEntry) {
        fileEntry.createWriter(function(fileWriter) {
          var truncated = false;
          var blob = new Blob([textToSave], { type: 'text/plain' });

          fileWriter.onwriteend = function() {
            if (!truncated) {
              truncated = true;
              this.truncate(this.position);
              return;
            }

            status.textContent = 'Text saved to ' + filename + ' in ' + directoryEntry.fullPath;
          };

          fileWriter.onerror = function(e) {
            status.textContent = 'Error saving text: ' + e.toString();
          };

          fileWriter.write(blob);
        });
      });
    });
  });
});