/**
*
* Module Lang Select
* Author: Noe Sanchez
* Handles the selection of language Store. 
* 
**/

var langSelect = (function ($) {
	var ls = {
		init: function(){
			this.cache();
			this.bind();
			return this;
		},
		cache: function(){
			var form = $('#language_selector');
			var select = form.find('select.LangSelect-sct');

			if (form.length > 0) { 
				this.form = form;
				this.select = select;
			};
		},
		bind: function(){
			this.select.on('change', function onSelectChange (e) {
				this.form.submit();
			});
		}
	};
	return ls.init();
})(jQuery);