// Models for Offline Contact app

// Global backbone app
var App = App || {};

(function(){
  'use strict';

  App.ContactModel = Backbone.Model.extend({
    defaults: {
      name: 'Noname'
    },
    idAttribute: 'id'
  });

})();