module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    compass: {
      dist: {
        options: {
          sassDir: 'sass',
          cssDir: 'stylesheets',
          outputStyle: 'compressed',
          noLineComments: true
        }
      },
    },
    csslint: {
      strict: {
        options: {
          'box-sizing': false,
          import: 2
        },
        src: ['stylesheets/leticia.css']
      }
    },
    watch: {
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

  grunt.registerTask('css', ['compass', 'csslint'])
  grunt.registerTask('default', ['css']);

};
