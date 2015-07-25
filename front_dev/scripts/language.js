/**
*
* Module Lang Select
* Author: Noe Sanchez
* Handles the selection of language Store. 
* 
**/

var LangSelect = (function ($) {
	var language = {
		init: function(){
			console.log('running language select');
			this.cache();
			this.bind();
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
	return language;
})(jQuery);