var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

gulp.task('styles', function() {
   return $.rubySass('styles/',{ compass:true})
   	.on('error', function (err){
   		console.log('Error!', err.message);
   	})
   	.pipe(gulp.dest('../static/styles/'));
});

gulp.task('scripts', function() {
	return gulp.src('scripts/*.js')
	  .pipe($.concat('all.js'))
	  .pipe(gulp.dest('../static/scripts/'));
});

gulp.task('watch',function() {
	gulp.watch('styles/**/*.scss',['styles']);
	gulp.watch(['scripts/*.js', 'scripts/**/*.js'],['scripts']);
});