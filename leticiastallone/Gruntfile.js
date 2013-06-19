module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    jslint: {
      files: ['static/javascripts/leticia.js'],
      directives: {
        browser: true,
        unparam: true,
        todo: true
      }
    },
    uglify: {
      build: {
        src: 'static/javascripts/leticia.js',
        dest: 'static/javascripts/leticia.min.js'
      }
    },
    compass: {
      dist: {
        options: {
          sassDir: 'sass',
          cssDir: 'static/stylesheets',
          outputStyle: 'compressed',
          noLineComments: true
        }
      },
    },
    csslint: {
      strict: {
        options: {
          'box-sizing': false,
          'qualified-headings': false,
          'font-sizes': false,
          import: 2
        },
        src: ['static/stylesheets/leticia.css']
      }
    },
    watch: {
      scripts: {
        files: ['static/javascripts/leticia.js'],
        tasks: ['js'],
        options: {
          debounceDelay: 250,
        }
      },
      styles: {
        files: 'sass/**/*.scss',
        tasks: ['css'],
        options: {
          debounceDelay: 250,
        },
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-csslint');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-jslint');

  grunt.registerTask('js', ['jslint', 'uglify']);
  grunt.registerTask('css', ['compass', 'csslint'])
  grunt.registerTask('default', ['css', 'js']);
};
