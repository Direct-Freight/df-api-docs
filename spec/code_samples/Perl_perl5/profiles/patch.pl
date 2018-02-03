#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new("PATCH",
"https://www.directfreight.com/api/profiles");
$request->content('{"address":"<ADD STRING VALUE>","city":"<ADD STRING VALUE>","company":"<ADD STRING VALUE>","contact_extension":"<ADD STRING VALUE>","contact_name":"<ADD STRING VALUE>","contact_number":"<ADD STRING VALUE>","dot_number":"<ADD STRING VALUE>","fax_number":"<ADD STRING VALUE>","mc_number":"<ADD STRING VALUE>","mobile_carrier":0,"mobile_number":"<ADD STRING VALUE>","state":"<ADD STRING VALUE>","web_page":"<ADD STRING VALUE>","zip":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print Dumper($response->json_content);