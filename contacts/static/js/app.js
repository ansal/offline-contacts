// Contact app

// Global backbone app
var App = App || {};

(function(){
  'use strict';

  new App.MainView();
  App.contacts.fetch({
    reset: true
  });

})();