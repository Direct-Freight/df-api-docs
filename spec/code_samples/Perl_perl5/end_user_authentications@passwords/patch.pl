#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(PATCH,
"https://www.directfreight.com/api/end_user_authentications/passwords")
$request->content('{"new_password":"<ADD STRING VALUE>","old_password":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;