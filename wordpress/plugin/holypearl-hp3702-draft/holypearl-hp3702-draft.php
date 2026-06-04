<?php
/**
 * Plugin Name: HolyPearl Homepage Draft 3702
 * Description: Renders the intent-based homepage on draft page 3702 only. Does not change live homepage (page 52).
 * Version: 1.0.0
 * Author: HolyPearl / פנינת הקודש
 * Text Domain: holypearl-hp3702
 * Requires at least: 6.0
 * Requires PHP: 7.4
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HP3702_PAGE_ID', 3702 );
define( 'HP3702_PLUGIN_FILE', __FILE__ );
define( 'HP3702_PLUGIN_DIR', plugin_dir_path( __FILE__ ) );

/**
 * Is the current request for draft homepage page 3702?
 */
function hp3702_is_target_page() {
	return is_page( HP3702_PAGE_ID );
}

/**
 * Load homepage CSS from assets.
 */
function hp3702_get_css() {
	$file = HP3702_PLUGIN_DIR . 'assets/homepage-intent-draft-3702.css';
	if ( ! is_readable( $file ) ) {
		return '';
	}
	$css = file_get_contents( $file );
	return $css ? $css : '';
}

/**
 * Load homepage HTML from assets.
 */
function hp3702_get_markup() {
	$file = HP3702_PLUGIN_DIR . 'assets/homepage-content.html';
	if ( ! is_readable( $file ) ) {
		return '<p>HolyPearl HP3702: homepage markup file missing.</p>';
	}
	$html = file_get_contents( $file );
	return $html ? $html : '';
}

/**
 * Disable Beaver Builder layout on page 3702 so our markup replaces it.
 */
function hp3702_disable_beaver_builder() {
	if ( ! hp3702_is_target_page() ) {
		return;
	}

	add_filter( 'fl_builder_is_enabled', '__return_false', 99 );
	add_filter( 'fl_builder_render_shortcodes', '__return_false', 99 );
}

add_action( 'wp', 'hp3702_disable_beaver_builder', 1 );

/**
 * Body class for Astra layout tweaks.
 */
function hp3702_body_class( $classes ) {
	if ( hp3702_is_target_page() ) {
		$classes[] = 'holypearl-hp3702-active';
	}
	return $classes;
}

add_filter( 'body_class', 'hp3702_body_class' );

/**
 * Hide default page title on 3702.
 */
function hp3702_hide_title( $enabled ) {
	if ( hp3702_is_target_page() ) {
		return false;
	}
	return $enabled;
}

add_filter( 'astra_the_title_enabled', 'hp3702_hide_title' );

/**
 * Enqueue fonts and inline CSS.
 */
function hp3702_enqueue_assets() {
	if ( ! hp3702_is_target_page() ) {
		return;
	}

	wp_enqueue_style(
		'hp3702-fonts',
		'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap&subset=hebrew,latin',
		array(),
		null
	);

	wp_register_style( 'holypearl-hp3702-draft', false, array( 'hp3702-fonts' ) );
	wp_enqueue_style( 'holypearl-hp3702-draft' );
	wp_add_inline_style( 'holypearl-hp3702-draft', hp3702_get_css() );
}

add_action( 'wp_enqueue_scripts', 'hp3702_enqueue_assets', 20 );

/**
 * Replace page content with intent homepage markup.
 */
function hp3702_replace_content( $content ) {
	if ( ! hp3702_is_target_page() || ! in_the_loop() || ! is_main_query() ) {
		return $content;
	}

	static $rendered = false;
	if ( $rendered ) {
		return '';
	}
	$rendered = true;

	return hp3702_get_markup();
}

add_filter( 'the_content', 'hp3702_replace_content', 99999 );
