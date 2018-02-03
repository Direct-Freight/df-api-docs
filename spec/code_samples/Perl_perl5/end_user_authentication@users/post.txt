#!/usr/bin/perl
use Modern::Perl;
use HTTP::Request::JSON;
use LWP::UserAgent::JSON;
my $request = HTTP::Request::JSON->new(%s,
"POST") https://www.directfreight.com/api/end_user_authentication/users
$request->content('{"email":"<ADD STRING VALUE>","end-user-token":"<ADD STRING VALUE>","password":"<ADD STRING VALUE>"}');
my $browser = LWP::UserAgent::JSON->new();
my $response = $browser->request($request);
print $response->json_content;