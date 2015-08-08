var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var mainBowerFiles = require('main-bower-files');

gulp.task('styles', function() {
   return $.rubySass('styles/',{ compass:true})
   	.on('error', function (err){
   		console.log('Error!', err.message);
   	})
   	.pipe(gulp.dest('../static/styles/'));
});

gulp.task('scripts', function() {
	return gulp.src([
			'scripts/language.js',
            'scripts/search.js',
			'scripts/minibasket.js',
			'scripts/main.js'
		])
	  .pipe($.concat('main.js'))
	  .pipe(gulp.dest('../static/scripts/'));
});

gulp.task('bower', function() {
	var jsFilter = $.filter('**/*.js');
	var cssFilter = $.filter('**/*.css');
	
  gulp.src(mainBowerFiles())
    .pipe(jsFilter)
    .pipe($.concat('bundle.js'))
    .pipe($.uglify())
    .pipe(gulp.dest('../static/scripts/'))
    .pipe(jsFilter.restore())
    .pipe(cssFilter)
    .pipe($.concatCss('styles/bundle.css'))
    .pipe($.csso())
    .pipe(gulp.dest('../static/'));
});

gulp.task('watch',function() {
	gulp.watch('styles/**/*.scss',['styles']);
	gulp.watch(['scripts/*.js', 'scripts/**/*.js'],['scripts']);
});