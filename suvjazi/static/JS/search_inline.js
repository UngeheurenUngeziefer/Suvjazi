(function() {
    var searchbox = $('#search'),
        autocomplete = $('#search-autocomplete'),
        loadMoreButton = $('.load-more', autocomplete),
        spinner = $('.loader', autocomplete),
        noResults = $('.no-results', autocomplete),
        error = $('.error', autocomplete);
    
    var currentOffset = 0,
        // some random URL to load because we don't use the result anyway, just so the request will succeed :P
        searchUrl = 'https://raw.githubusercontent.com/ghosh/uiGradients/master/gradients.json', //'https://www.crossorigin.me/https://ajax.googleapis.com/ajax/services/search/web',
        lastSearch = '',
        searchTimeout = 0.5, //seconds
        searchTimer;
  
    function loadData() {
      noResults.hide();
      error.hide();
      loadMoreButton.hide();
      spinner.show();
      
      if(searchbox.val() !== lastSearch) {
        $('.search-result', autocomplete).remove();
        currentOffset = 0;
      }
  
      lastSearch = searchbox.val();
      
      $.ajax({
        type: 'GET',
        url: searchUrl,
        dataType: 'text',
        data: {
          'v': '1.0',
          'q': lastSearch,
          'start': currentOffset
        },
        success: function(data) {
          // Since the web search API is dead we have to fake it for the demo
          // Can't be bothered to actually remove the AJAX request so it stays ;)
          data = '{"responseData": {"results" : [{"url": "https://www.google.com","titleNoFormatting": "Quibusdam minus","content": "Quibusdam minus saepe incididunt tincidunt congue repellendus malesuada pretium veniam explicabo molestiae cupiditate natoque praesentium nascetur, vitae anim risus soluta quisque aliquip harum modi? Maecenas esse culpa mattis! Natus voluptatum."},{"url": "https://www.google.com","titleNoFormatting": "Possimus! Quia, atque illo","content": "Possimus! Quia, atque illo imperdiet quam, lacus penatibus bibendum cupiditate? Nihil pellentesque velit voluptatem sodales lacus tellus torquent. Deserunt eum incidunt et."},{"url": "https://www.google.com","titleNoFormatting": "Cubilia amet eos proident","content": "Cubilia amet eos proident blandit irure nobis diam! Dignissim sed officiis aut, arcu, nulla necessitatibus fermentum officia fermentum."},{"url": "https://www.google.com","titleNoFormatting": "Wisi, rhoncus consectetuer","content": "Dictum iure blandit cupidatat, laborum potenti cupidatat magnam nostrum nibh! Wisi, rhoncus consectetuer netus! Enim vitae mollis ullamcorper fames eiusmod?"},{"url": "https://www.google.com","titleNoFormatting": "Cras tempore inventore","content": "Debitis cum auctor, nibh, etiam! Cras tempore inventore, nascetur possimus."}]}}';
          
          var json = $.parseJSON(data);
          
          if(json &&
             json.responseData &&
             json.responseData.results &&
             json.responseData.results.length > 0) {
            for(var i = 0; i < json.responseData.results.length; ++i) {
              $('<li class="search-result">' +
                  '<a href="'+ json.responseData.results[i].url +'" target="_blank">' +
                    json.responseData.results[i].titleNoFormatting +
                    '<span class="search-description">' +
                      json.responseData.results[i].content +
                    '</span>' +
                  '</a>' +
                '</li>').insertBefore(loadMoreButton);
            }
            
            noResults.hide();
            loadMoreButton.show();
            error.hide();
          } else {
            noResults.show();
            loadMoreButton.hide();
            error.hide();
          }
          
          if(json &&
             !json.responseData &&
              json.responseDetails) {
            noResults.hide();
            loadMoreButton.hide();
            error.text(json.responseDetails).show();
            console.error(json.responseDetails);
          }
          
          spinner.hide();
          currentOffset += json.responseData.results.length;
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.error(errorThrown);
          
          error.text(textStatus + ': ' + errorThrown).show();
          
          loadMoreButton.hide();
          noResults.hide();
          spinner.hide();
        }
      });
    }
    
    searchbox.on('focus', function() {
      if($(this).val().length > 0) {
        autocomplete.slideDown('fast');
      }
    })
    .on('input propertychange paste', function() {
      //this will handle pasting text and clearing text with browser built in clear button
      $(this).trigger('keyup');
    })
    .on('keydown', function() {
      clearTimeout(searchTimer);
    })
    .on('keyup', function() {
      if($(this).val().length > 0) {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(loadData, searchTimeout * 1000);
        autocomplete.slideDown('fast');
      } else {
        clearTimeout(searchTimer);
        autocomplete.slideUp('fast');
      }
    });
  
    $(document).on('click', function(e) {
      //click anywhere outside searchbox to close
      if(!$(e.target).closest('.searchbox').length) {
        if(autocomplete.is(':visible')) {
          autocomplete.slideUp('fast');
          clearTimeout(searchTimer);
        }
      }
    });
  
    
    autocomplete.css('top', (searchbox.outerHeight()) + 'px');
    loadMoreButton.on('click', loadData)
                  .hide();
    noResults.hide();
    error.hide();
    
  }());