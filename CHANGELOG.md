Change Log
==========


<!-- ## Unreleased (../../compare/v0.4.3...master) -->

## [0.4.3](../../compare/v0.4.2...v0.4.3) - 2021-07-22 

Fixed: 
* require gi >= 3.28 [#26](../../pull/26)

Changed:
* [Using Github actions for CI](https://github.com/hnesk/browse-ocrd/actions/workflows/unittest.yml)
* Get rid of DEFAULT_FILE_GROUP = 'OCR-D-IMG'
* Silence xsd error messages on stderr, when reading files produced by ocrd-cis-align 

New Features:
* Added a Diff-View [#13](../../issues/13) & [#29](../../pull/29)

## [0.4.2](../../compare/v0.4.1...v0.4.2) - 2020-11-12 

Fixed: 

* Catch empty imageFilename case &  don't download remote urls upfront [#25](../../issues/25)  
* Pillow workaround: convert 16-bit images to 8-bit [#23](../../pull/23)
* Don't crash on unhandled mimetype [#18](../../issues/18)
* typing.OrderedDict is not available in python 3.6  [#22](../../issues/22)

New Features

* Views can be resized and splitted now [#12](../../issues/12) 
* Added Webkit-HTML-View for [dinglehopper](https://github.com/qurator-spk/dinglehopper) [#25](../../pull/25) (partially fixes [#13](../../issues/13))
* Added a button to launch [PageViewer](https://www.primaresearch.org/tools/PAGEViewer) from XmlView [#21](../../pull/21) 


## [0.4.1](../../compare/v0.4.0...v0.4.1) - 2020-10-30

Fixed:

* Fix segfault: Dont put scrollable Gtk.Viewports in scrollable Gtk.Sourceviews / Removes self.viewport from View / Fixes #17
* chdir to workspace directory, fixes #19

## [0.4.0](../../compare/v0.3.0...v0.4.0) - 2020-10-22

Changed:

* Introduce Zoom #14
* show all derived images per page #14
* add Text view (simple concatenated) #10 
  
Fixed:
*  Support conversion of PIL LA image via cv #5
*  adapt to ocrd>=2.17 logging #6 

## [0.3.0](../../compare/v0.1.9...v0.3.0) - 2020-08-13

A lot:
* Found a basic structure 
* Started unittests
* Implement [scanning](https://github.com/hnesk/browse-ocrd-physical-import) as an extension

## [0.1.9] - 2020-08-01

First more or less public release 



