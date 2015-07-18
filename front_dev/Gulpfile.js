var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

gulp.task('styles', function() {
   return $.rubySass('styles/',{ compass:true})
   	.on('error', function (err){
   		console.log('Error!', err.message);
   	})
   	.pipe(gulp.dest('../static/styles/'));
});

gulp.task('watch',function() {
	gulp.watch(['styles/*.scss', 'styles/**/*.scss'],['styles']);
});