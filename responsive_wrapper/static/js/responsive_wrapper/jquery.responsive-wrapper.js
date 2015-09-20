// the semi-colon before function invocation is a safety net against concatenated
// scripts and/or other plugins which may not be closed properly.
;(function($, window, document, undefined) {

  var render = 'render';

  function ResponsiveWrapper(el, options) {
    this.el = $(el);
    this.settings = $.extend({}, defaults, options);
    this._defaults = defaults;
    this._name = render;
    this.ajaxUrl = this.el.data('ajaxUrl');
    this.init();
  }

  ResponsiveWrapper.prototype = {
    init: function() {
      $(window).on('resize load', this.debounce(function() {
        this.onResize();
      }.bind(this), 300));
    },
    debounce : function (func, delay, immediate) {
      var timeout, result;
      return function () {
        var context = this, args = arguments;
        var later = function () {
          timeout = null;
          if (!immediate) {
            result = func.apply(context, args);
          }
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, delay);
        if (callNow) {
          result = func.apply(context, args);
        }
        return result;
      };
    },
    onResize: function() {
      var that = this;
      $.get(this.ajaxUrl, {
        width: $(window).width(),
        height: $(window).height(),
        dpr: window.devicePixelRatio || (window.screen.deviceXDPI / window.screen.logicalXDPI) || 1
      }, function(response) {
        that.el.html(response);
        that.el.trigger('rendered');
      });
    }
  };

  $.fn[render] = function(options) {
    return this.each(function() {
      if (!$.data(this, 'plugin_' + render)) {
        $.data(this, 'plugin_' + render, new ResponsiveWrapper(this, options));
      }
    });
  };

})(jQuery, window, document);
