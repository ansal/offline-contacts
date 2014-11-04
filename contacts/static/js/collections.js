// Collections for Offline Contact app

// Global backbone app
var App = App || {};

(function(){
  'use strict';

  var ContactCollection = Backbone.Collection.extend({
    model: App.ContactModel,
    url: '/names/api/contact/'
  });

  App.contacts = new ContactCollection;

})();