// the semi-colon before function invocation is a safety net against concatenated
// scripts and/or other plugins which may not be closed properly.
;(function ( $, window, document, undefined ) {

    var interchange = 'interchange',
        defaults = {
            propertyName: 'value'
        };

    // The actual plugin constructor
    function Interchange (element, options ) {
        this.element = $(element);
        this.settings = $.extend({}, defaults, options);
        this._defaults = defaults;
        this._name = interchange;
        this.init();
    }

    Interchange.prototype = {
        init: function () {
            console.log('xD');
        },
        yourOtherFunction: function () {
            // some logic
        }
    };

    $.fn[interchange] = function (options) {
        return this.each(function() {
            if ( !$.data( this, 'plugin_' + interchange ) ) {
                $.data( this, 'plugin_' + interchange, new Interchange(this, options) );
            }
        });
    };

})(jQuery, window, document);
