#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(POST,
"https://www.directfreight.com/api/alerts/%7Balert_type%7D")
$request->content('{"days_of_week":{},"email_address":"<ADD STRING VALUE>","end_hour":{},"expires_after":{},"list_order":{},"list_type":{},"minute_frequency":{},"send_type":{},"start_hour":{},"time_zone":{}}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;