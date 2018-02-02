use Data::Dumper;

# Configure API key authorization: api_key
$WWW::SwaggerClient::Configuration::api_key->{'api-token'} = 'YOUR_API_KEY';
# uncomment below to setup prefix (e.g. Bearer) for API key, if needed
#$WWW::SwaggerClient::Configuration::api_key_prefix->{'api-token'} = "Bearer";

my $api_instance = WWW::SwaggerClient::BoardsApi->new();
my $body = WWW::SwaggerClient::Object::SearchBoard->new(); # SearchBoard | 
my $board_type = 'board_type_example'; # string | This will be specified in the url. Valid types are \"loads\", and \"trucks\".
my $end_user_token = 'end_user_token_example'; # string | Sensitive info like phone numbers won't be returned without this.

eval { 
    my $result = $api_instance->boards_board_type_post(body => $body, board_type => $board_type, end_user_token => $end_user_token);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling BoardsApi->boards_board_type_post: $@\n";
}
