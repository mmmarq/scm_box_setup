<?php
$g_hostname               = 'mysql.raspberry.pi';
$g_db_type                = 'mysqli';
$g_database_name          = 'bugtracker';
$g_db_username            = 'bugs';
$g_db_password            = 'bugless';

$g_default_timezone       = 'UTC';

$g_crypto_master_salt     = 'hIQ5m/FtwreZ8CQQ8cw9qUgASeIkQ3aM8EoPYeFUdp0=';
$g_cookie_path            	= '/mantisbt/';


# --- Anonymous Access / Signup ---
$g_allow_signup			= OFF;
$g_allow_anonymous_login	= OFF;
$g_anonymous_account		= '';


# --- Branding ---
$g_window_title			= 'Raspberry Pi SCM in a Box - MantisBT';
# $g_logo_image			= 'images/mantis_logo.png';
# $g_favicon_image		= 'images/favicon.ico';


# --- Email Configuration ---
$g_enable_email_notification    = SMTPONOFF;
$g_phpMailer_method             = PHPMAILER_METHOD_SMTP;
$g_smtp_host                    = 'SMTPSERVER';
$g_smtp_username                = 'SMTPUSER';
$g_smtp_password                = 'SMTPPASSWD';
$g_smtp_port                    = 'SMTPPORT';
$g_from_email           	= 'noreply@raspberry.pi';
$g_return_path_email    	= 'admin@raspberry.pi';


# --- LDAP Configuration ---
$g_login_method 		= LDAP;
$g_ldap_protocol_version 	= 3;
$g_ldap_server 			= 'ldap://ldap.raspberry.pi';
$g_ldap_root_dn 		= 'ou=people,dc=ldap,dc=raspberry,dc=pi';
$g_use_ldap_email 		= ON;
$g_ldap_realname_field 		= 'givenname';
$g_use_ldap_realname 		= ON;


# --- Log Configuration ---
#$g_display_errors = array(
#	E_USER_ERROR   => DISPLAY_ERROR_INLINE,
#	E_USER_WARNING => DISPLAY_ERROR_INLINE,
#	E_WARNING      => DISPLAY_ERROR_INLINE,
#);
#$g_show_detailed_errors = ON;
#$g_log_level 			= LOG_ALL;
#$g_log_destination 		= 'file:/my_services/mantisbt/logs/mantis.log';

# --- Web Service configuration ---
$g_webservice_readonly_access_level_threshold =
$g_webservice_readwrite_access_level_threshold =
$g_webservice_admin_access_level_threshold = MANAGER;
