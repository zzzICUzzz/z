function findRelatedFiles(event) {
    event.preventDefault();
    var input = document.getElementById('inputSearch').value;
    input = input.toLowerCase().replace(/[^a-z]/g, '');
  
    fetch('d/trans.json')
      .then(response => response.json())
      .then(jsonData => {
        var targets = Object.keys(jsonData).map(key => ({file: jsonData[key], fileName: key}));
        var results = fuzzysort.go(input, targets, {key: 'file'});
  
        var resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';
        results.slice(0, 15).forEach((result, index) => { // Chỉ lấy 15 kết quả đầu tiên
          var div = document.createElement('div');
          div.classList.add('selections');
          div.style.animationDelay = `${index * 0.1}s`;
          var link = document.createElement('a');
          link.href = '/z/d/html/' + result.obj.fileName;
          link.textContent = result.obj.file;
          div.appendChild(link);
          resultsDiv.appendChild(div);
        });
      })
      .catch(error => console.error('Có lỗi xảy ra:', error));
  }
  
  document.getElementById('inputSearch').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      findRelatedFiles(event);
    }
  });
  
