ex_swde_prompt = {
    'meta': 'It\'s worth noticing that the candidate attribute values are the non-empty strings contained in text nodes in the corresponding DOM tree, and one page may contain multiple distinct values that correspond to an attribute.',
    'movie-allmovie(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'AMG Work ID': "Please extract the 'AMG Work ID' of the movie.", 
        'Category': "Please extract the 'Category' of the movie.", 
        'Color Type': "Please extract the 'Color Type' of the movie.", 
        'Countries': "Please extract the 'Countries' of the movie.", 
        'Director': "Please extract the 'Director' of the movie.", 
        'Flags': "Please extract the 'Flags' of the movie.", 
        'Genres': "Please extract the 'Genres' of the movie.", 
        'Keywords': "Please extract the 'Keywords' of the movie.", 
        'MPAA Rating': "Please extract the 'MPAA Rating' of the movie.", 
        'Moods': "Please extract the 'Moods' of the movie.", 
        'Other Related Works | Is related to:': "Please provide the details about other works related to the movie.", 
        'Plot Synopsis': "Please extract the 'Plot Synopsis' of the movie.", 
        'Produced by': "Please provide information about who produced the movie.", 
        'Run Time': "Please extract the 'Run Time' of the movie.", 
        'Similar Works': "Please extract the 'Similar Works' of the movie.", 
        'Themes': "Please extract the 'Themes' of the movie.", 
        'Tones': "Please extract the 'Tones' of the movie.", 
        'Types': "Please extract the 'Types' of the movie.", 
        'Year': "Please extract the 'Year' of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
        },
    'movie-amctv(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Category:': "Please extract the 'Category' of the movie.", 
        'Country:': "Please extract the 'Country' of the movie.", 
        'Director:': "Please extract the 'Director' of the movie.", 
        'Filmed In:': "Please provide the filming location details of the movie.", 
        'Genre/Type:': "Please extract the 'Genre/Type' of the movie.", 
        'Key Cast:': "Please extract the 'Key Cast' of the movie.", 
        'Keywords:': "Please extract the 'Keywords' of the movie.", 
        'Language:': "Please extract the 'Language' of the movie.", 
        'MPAA Rating:': "Please extract the 'MPAA Rating' of the movie.", 
        'Produced By:': "Please provide information about who produced the movie.", 
        'Run Time:': "Please extract the 'Run Time' of the movie.", 
        'Themes:': "Please extract the 'Themes' of the movie.", 
        'Year:': "Please extract the 'Year' of the movie."
    },
    'movie-hollywood(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Full Cast & Crew | Art Department | Production Designer': "Please provide the details of the movie's full cast and crew, specifically focusing on the art department and the production designer.", 
        'Full Cast & Crew | Cast': "Please provide the list of the full cast from the movie.", 
        'Full Cast & Crew | Director': "Please provide information about the director of the movie.", 
        'Full Cast & Crew | Distribution Companies': "Please extract the information about the distribution Companies of the movie.", 
        'Full Cast & Crew | Film Camera | Cinematographer': "Please provide information about the cinematographer from the film camera team of the movie.", 
        'Full Cast & Crew | Music | Composer (Music Score)': "Please provide information about the composer of the movie.", 
        'Full Cast & Crew | Producers | Producer': "Please extract the Producers of the movie.", 
        'Full Cast & Crew | Wardrobe Hair Makeup | Costume Designer': "Please provide information about the costume designer from the wardrobe, hair, and makeup team of the movie.", 
        'Full Cast & Crew | Writer | Screenwriter': "Please extract the Screenwriter of the movie.", 
        'Synopsis': "Please extract the 'Synopsis' of the movie.", 
        'Theatrical Release': "Please extract the 'Theatrical Release' of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
        
    },
    'movie-iheartmovies(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Directed by': "Please extract the Director of the movie.", 
        'Genres': "Please extract the 'Genres' of the movie.", 
        'Language': "Please extract the 'Language' of the movie.", 
        'Length': "Please extract the 'Length' of the movie.", 
        'MPAA Rating': "Please extract the 'MPAA Rating' of the movie.", 
        'Released': "Please extract the 'Released' of the movie.", 
        'Written by': "Please extract the writter of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
    },
    'movie-imdb(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Box Office | Budget:': "Please extract the Budget of the movie.", 
        'Box Office | Gross:': "Please extract the Gross of the movie.", 
        'Box Office | Opening Weekend:': "Please extract the Opening Weekend of the movie.", 
        'Company Credits | Production Co:': "Please extract the Production Co of the movie.", 
        'Critics:': "Please extract the 'Critics' of the movie.", 
        'Details | Also Known As:': "Please provide the alternative titles the movie is known by.", 
        'Details | Country:': "Please extract the Country of the movie.", 
        'Details | Filming Locations:': "Please extract the Filming Locations of the movie.", 
        'Details | Language:': "Please extract the Language of the movie.", 
        'Details | Release Date:': "Please extract the Release Date of the movie.", 
        'Director:': "Please extract the Director of the movie.", 
        'Full cast and crew | Cast overview, first billed only: | Cast': "Please provide the list of the main cast members of the movie, starting with the top-billed actors.", 
        'Fun Facts | Connections': "Please extract the Connections of the movie.", 
        'Fun Facts | Goofs': "Please extract the Goofs of the movie.", 
        'Fun Facts | Quotes': "Please extract the Quotes of the movie.", 
        'Fun Facts | Soundtracks': "Please extract the Soundtracks of the movie.", 
        'Fun Facts | Trivia': "Please extract the Trivia of the movie.", 
        'Genres:': "Please extract the 'Genres' of the movie.", 
        'MPAA | Motion Picture Rating': "Please extract the Motion Picture Rating of the movie.", 
        'Message Boards': "Please extract the Message Boards of the movie.", 
        'Plot Keywords:': "Please extract the Plot Keywords of the movie.", 
        'Recommendations': "Please extract the Recommendations of the movie.", 
        'Related Lists': "Please extract the Related Lists of the movie.", 
        'Related News': "Please extract the Related News of the movie.", 
        'Stars:': "Please extract the Stars of the movie.", 
        'Storyline': "Please extract the Storyline of the movie.", 
        'Taglines:': "Please extract the Taglines of the movie.", 
        'Technical Specs | Aspect Ratio:': "Please extract the Aspect Ratio of the movie.", 
        'Technical Specs | Color': "Please extract the Color of the movie.", 
        'Technical Specs | MOVIEmeter:': "Please extract the MOVIEmeter of the movie.", 
        'Technical Specs | Runtime:': "Please extract the Runtime of the movie.", 
        'Technical Specs | Sound Mix:': "Please extract the Sound Mix of the movie.", 
        'Users: (': "Please extract the Users of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
    },
    'movie-metacritic(2000)' : {
    'meta': 'Here\'s a webpage on detail information of a movie.',
    'Critic Reviews | Mixed: | Mixed&&&Critic Reviews': "Please extract the Critic Reviews of the movie.", 
    'Critic Reviews | Negative: | Negative&&&Critic Reviews': "Please extract the Negative Critic Reviews of the movie.", 
    'Critic Reviews | Positive: | Positive&&&Critic Reviews': "Please extract the Positive Critic Reviews of the movie.", 
    'Director:': "Please extract the Director of the movie.", 
    'Genre(s):': "Please extract the Genre(s) of the movie.", 
    'Metascore': "Please extract the Metascore of the movie.", 
    'Rating:': "Please extract the Rating of the movie.", 
    'Release Date:': "Please extract the Release Date of the movie.", 
    'Reviewed by:': "Please provide the reviewer's information.", 
    'Runtime:': "Please extract the Runtime of the movie.", 
    'Starring:': "Please extract the Starring of the movie.", 
    'Studio:': "Please extract the Studio of the movie.", 
    'User Reviews | Mixed: | Mixed&&&User Reviews': "Please extract the User Reviews of the movie.", 
    'User Reviews | Negative: | Negative&&&User Reviews': "Please extract the Negative User Reviews of the movie.", 
    'User Reviews | Positive: | Positive&&&User Reviews': "Please extract the Positive User Reviews of the movie.", 
    'User Score': "Please extract the 'User Score' of the movie.", 'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
    },
    'movie-rottentomatoes(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Cast': "Please extract the Cast of the movie.", 
        'Directed By:': "Please extract the Director of the movie.", 
        'Distributor:': "Please extract the Distributor of the movie.", 
        'Genre:': "Please extract the Genre of the movie.", 
        'In Theaters:': "Please provide the movie's theater release date.", 
        'Rated:': "Please extract the Rated of the movie.", 
        'Running Time:': "Please extract the Running Time of the movie.", 
        'Synopsis:': "Please extract the Synopsis of the movie.", 
        'Written By:': "Please extract the 'Writter of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
    },
    'movie-yahoo(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a movie.',
        'Cast and Credits | Directed by:': "Please extract the Director of the movie.", 
        'Cast and Credits | Produced by:': "Please extract the Producer of the movie.", 
        'Cast and Credits | Starring:': "Please extract the Starring of the movie.", 
        'Genres:': "Please extract the Genres of the movie.", 
        'MPAA Rating:': "Please extract the MPAA Rating of the movie.", 
        'Release Date:': "Please extract the Release Date of the movie.", 
        'Running Time:': "Please extract the Running Time of the movie.", 
        'U.S. Box Office:': "Please extract the U.S. Box Office of the movie.", 
        'Yahoo! Users:': "Please extract the Yahoo Users of the movie.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the movie."
        },
    'nbaplayer-espn(434)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'Age': "Please extract the 'Age' of the nbaplayer.", 
        'Birth Date': "Please extract the 'Birth Date' of the nbaplayer.", 
        'Birth Place': "Please extract the 'Birth Place' of the nbaplayer.", 
        'Height': "Please extract the 'Height' of the nbaplayer.", 
        'Next Game:': "Please extract the 'Next Game' of the nbaplayer.", 
        'PPG': "Please extract the 'PPG' of the nbaplayer.", 
        'Position': "Please extract the 'Position' of the nbaplayer.", 
        'Salary': "Please extract the 'Salary' of the nbaplayer.", 
        'Weight': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-fanhouse(446)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'APG': "Please extract the 'APG' of the nbaplayer.", 
        'Age': "Please extract the 'Age' of the nbaplayer.", 
        'Birthplace': "Please extract the 'Birthplace' of the nbaplayer.", 
        'Born': "Please extract the 'Born' of the nbaplayer.", 
        'College': "Please extract the 'College' of the nbaplayer.", 
        'Experience': "Please extract the 'Experience' of the nbaplayer.", 
        'Height': "Please extract the 'Height' of the nbaplayer.", 
        'Name': "Please extract the 'Name' of the nbaplayer.", 
        'PPG': "Please extract the 'PPG' of the nbaplayer.", 
        'Position': "Please extract the 'Position' of the nbaplayer.", 
        'RPG': "Please extract the 'RPG' of the nbaplayer.", 
        'Team': "Please extract the 'Team' of the nbaplayer.", 
        'Weight': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-foxsports(425)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'Age': "Please extract the 'Age' of the nbaplayer.", 
        'Born': "Please extract the 'Born' of the nbaplayer.", 
        'College': "Please extract the 'College' of the nbaplayer.", 
        'Ht': "Please extract the 'Ht' of the nbaplayer.", 
        'INJURY STATUS': "Please extract the 'INJURY STATUS' of the nbaplayer.", 
        'Impact': "Please extract the 'Impact' of the nbaplayer.", 
        'News': "Please extract the 'News' of the nbaplayer.", 
        'Source': "Please extract the 'Source' of the nbaplayer.", 
        'Wt': "Please extract the 'Wt' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-msnca(434)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'APG': "Please extract the 'APG' of the nbaplayer.", 
        'Birthplace:': "Please extract the 'Birthplace' of the nbaplayer.", 
        'Born:': "Please extract the 'Born' of the nbaplayer.", 
        'College:': "Please extract the 'College' of the nbaplayer.", 
        'Draft:': "Please extract the 'Draft' of the nbaplayer.", 
        'Height:': "Please extract the 'Height' of the nbaplayer.", 
        'PPG': "Please extract the 'PPG' of the nbaplayer.", 
        'Position:': "Please extract the 'Position' of the nbaplayer.", 
        'RPG': "Please extract the 'RPG' of the nbaplayer.", 
        'Team:': "Please extract the 'Team' of the nbaplayer.", 
        'Weight:': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-si(515)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'APG': "Please extract the 'APG' of the nbaplayer.", 
        'Age:': "Please extract the 'Age' of the nbaplayer.", 
        'Born:': "Please extract the 'Born' of the nbaplayer.", 
        'College:': "Please extract the 'College' of the nbaplayer.", 
        'FG%': "Please extract the 'FG%' of the nbaplayer.", 
        'Height:': "Please extract the 'Height' of the nbaplayer.", 
        'NBA Experience:': "Please extract the 'NBA Experience' of the nbaplayer.", 
        'PPG': "Please extract the 'PPG' of the nbaplayer.", 
        'RPG': "Please extract the 'RPG' of the nbaplayer.", 
        'Rookie Year:': "Please extract the 'Rookie Year' of the nbaplayer.", 
        'Weight:': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-slam(423)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'Assists/Game (APG)': "Please extract the 'Assists/Game (APG)' of the nbaplayer.", 
        'Birthdate': "Please extract the 'Birthdate' of the nbaplayer.", 
        'Birthplace': "Please extract the 'Birthplace' of the nbaplayer.", 
        'Blocks (BLK)': "Please extract the 'Blocks (BLK)' of the nbaplayer.", 
        'Games': "Please extract the 'Games' of the nbaplayer.", 
        'Height': "Please extract the 'Height' of the nbaplayer.", 
        'Points/Game (PPG)': "Please extract the 'Points/Game (PPG)' of the nbaplayer.", 
        'Position': "Please extract the 'Position' of the nbaplayer.", 
        'Rebounds/Game (RPG)': "Please extract the 'Rebounds/Game (RPG)' of the nbaplayer.", 
        'Steals': "Please extract the 'Steals' of the nbaplayer.", 
        'Weight': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'nbaplayer-usatoday(436)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'Age:': "Please extract the 'Age' of the nbaplayer.", 
        'DOB:': "Please extract the 'DOB' of the nbaplayer.", 
        'Height:': "Please extract the 'Height' of the nbaplayer.", 
        'Weight:': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
    },
    'nbaplayer-yahoo(438)' : {
        'meta': 'Here\'s a webpage on detail information of a nbaplayer.',
        'Ast': "Please extract the 'Ast' of the nbaplayer.", 
        'Born': "Please extract the 'Born' of the nbaplayer.", 
        'College': "Please extract the 'College' of the nbaplayer.", 
        'Draft': "Please extract the 'Draft' of the nbaplayer.", 
        'Height': "Please extract the 'Height' of the nbaplayer.", 
        'Pts': "Please extract the 'Pts' of the nbaplayer.", 
        'Reb': "Please extract the 'Reb' of the nbaplayer.", 
        'Weight': "Please extract the 'Weight' of the nbaplayer.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the nbaplayer."
        },
    'university-collegeprowler(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a university.',
        'Academic Calendar:': "Please extract the 'Academic Calendar' of the university.", 
        'Admission Difficulty:': "Please extract the 'Admission Difficulty' of the university.", 
        'Control:': "Please extract the 'Control' of the university.", 
        'FT Undergraduates:': "Please extract the 'FT Undergraduates' of the university.", 
        'Location:': "Please extract the 'Location' of the university.", 
        'Religious Affiliation:': "Please extract the 'Religious Affiliation' of the university.", 
        'School Contact': "Please extract the 'School Contact' of the university.", 
        'School Contact | *phone': "Please extract the phone of the university.", 
        'School Contact | *street address': "Please extract the street address of the university.", 
        'School Contact | *website': "Please extract the website of the university.", 
        'Setting:': "Please extract the 'Setting' of the university.", 
        'Tuition:': "Please extract the 'Tuition' of the university.", 
        'Undergrad Student Body | Full-Time:': "Please extract the Undergrad Student Body about Full-Time of the university.", 
        'Undergrad Student Body | Part-Time:': "Please extract the Undergrad Student Body about Part-Time of the university.", 
        'Undergrad Student Body | Total Female:': "Please extract the Undergrad Student Body about Total Female of the university.", 
        'Undergrad Student Body | Total Male:': "Please extract the Undergrad Student Body about Total Male of the university.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the university.", 
        'Cost | Books and Supplies:': "Please provide the cost of books and supplies at the university.", 
        },
    'university-ecampustours(1063)' : {
        'meta': 'Here\'s a webpage on detail information of a university.',
        'Degree Programs: | Highest degree offered:': "Please extract the Highest degree offered of the university.", 
        'Degrees Include:': "Please extract the all Degrees of the university.", 
        'Demographics | Affiliation': "Please extract the Affiliation of the university.", 
        'Demographics | Calendar System': "Please extract the Calendar System of the university.", 
        'Demographics | Enrollment*': "Please extract the Enrollment of the university.", 
        'Demographics | Institution': "Please extract the Institution of the university.", 
        'Demographics | Private School': "Please extract the Private School of the university.", 
        'Demographics | Student Body': "Please extract the Student Body of the university.", 
        'Demographics | Tuition*': "Please extract the Tuition of the university.", 
        'Demographics | Year Established': "Please extract the Year Established of the university.", 
        'School Details | *city/state/zip': "Please extract the city/state/zip of the university.", 
        'School Details | *website': "Please extract the website of the university.", 
        'School Details | Phone:': "Please extract the Phone of the university.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the university."
        },
    'university-embark(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a university.',
        'Application Information| Early Action Deadline:': "Please extract the Early Action Deadline of the university.", 
        'Application Information| Early Decision Deadline:': "Please extract the Early Decision Deadline of the university.", 
        'Application Information| Priority Application Deadline:': "Please extract the Priority Application Deadline of the university.", 
        'Application Information| Regular Application Deadline:': "Please extract the Regular Application Deadline of the university.", 
        'Cost and Financial Aid| Average Total Freshmen Need-based Aid:': "Please extract the Average Total Freshmen Need-based Aid of the university.", 
        'Cost and Financial Aid| Direct Lender:': "Please extract the Direct Lender of the university.", 
        'Cost and Financial Aid| In-State Tuition:': "Please extract the In-State Tuition of the university.", 
        'Cost and Financial Aid| Out-of-State Tuition:': "Please extract the Out-of-State Tuition of the university.", 
        'Cost and Financial Aid| Undergrads Receiving Need-based Financial Aid:': "Please extract the Undergrads Receiving Need-based Financial Aid of the university.", 
        'Phone:': "Please extract the Phone of the university.", 
        'Programs| ': "Please extract the Programs of the university.", 
        'Statistics| Average High School GPA:': "Please extract the Average High School GPA of the university.", 
        'Statistics| Average Math SAT:': "Please extract the Average Math SAT of the university.", 
        'Statistics| Average Verbal SAT:': "Please extract the Average Verbal SAT of the university.", 
        'Statistics| Degree Type:': "Please extract the Degree Type of the university.", 
        'Statistics| Enrollment:': "Please extract the Enrollment of the university.", 
        'Statistics| Most Popular Majors:': "Please extract the Most Popular Majors of the university.", 
        'Statistics| School Type:': "Please extract the School Type of the university.", 
        'Statistics| Setting:': "Please extract the Setting of the university.", 
        'Statistics| Student Faculty Ratio:': "Please extract the Student Faculty Ratio of the university.", 
        'topic_entity_name': "Please extract the 'topic_entity_name' of the university.", 
        'Fax:': "Please extract the Fax of the university.",
        'Statistics| ACT Composite Middle 50%:': "Please extract the 'ACT Composite Middle 50%' of the university.", 
        },
    'university-matchcollege(2000)' : {
        'meta': 'Here\'s a webpage on detail information of a university.',
        'Calendar System:': "Please extract the 'Calendar System' of the university.", 
        'Facilities and Programs Offered': "Please provide information about the facilities and programs offered by the university.", 
        'General Phone:': "Please extract the General Phone of the university.", 
        'Highest Degree:': "Please extract the Highest Degree of the university.", 
        'Local Area:': "Please extract the Local Area of the university.", 
        'OPEID College Code:': "Please extract the OPEID College Code of the university.", 
        'Overall Student Enrollment | Total Student Enrollment:': "Please extract the Total Student Enrollment of the university.", 
        'Source:': "Please extract the Source of the university.", 
        'Student Attendance | Total Student Attendance | Full-Time: | Total Student Attendance&&&Full-Time:': "Please provide details on the total number of students attending the university full-time.", 
        'Student Attendance | Total Student Attendance | Part-Time: | Total Student Attendance&&&Part-Time:': "Please provide details on the total number of students attending the university part-time.", 
        'Student Gender | Total Student Gender | Female: | Total Student Gender&&&Female:': "Please provide information on the total number of female students at the university.", 
        'Student Gender | Total Student Gender | Male: | Total Student Gender&&&Male:': "Please provide information on the total number of male students at the university.", 
        'Type:': "Please extract the Type of the university.", 
        'Website': "Please extract the Website of the university.", 
        'topic_entity_name': "Please extract the topic_entity_name of the university."
        },
    'university-usnews(1027)' : {
        'meta': 'Here\'s a webpage on detail information of a university.',
        'Admissions E-mail:': "Please extract the Admissions E-mail of the university.", 
        'College Category': "Please extract the College Category of the university.", 
        'Overview | General Information | 2009 Endowment:': "Please extract the 2009 Endowment of the university.", 
        'Overview | General Information | Academic calendar:': "Please extract the  Academic calendar of the university.", 
        'Overview | General Information | Fall Admissions | Application deadline': "Please extract the Application deadline of the university.", 
        'Overview | General Information | Fall Admissions | Application fee': "Please extract the Application fee of the university.", 
        'Overview | General Information | Fall Admissions | Fall 2009 acceptance rate': "Please extract the Fall 2009 acceptance rate of the university.", 
        'Overview | General Information | Fall Admissions | Selectivity': "Please extract the Selectivity of the university.", 
        'Overview | General Information | Institutional Control:': "Please extract the Institutional Control of the university.", 
        'Overview | General Information | Mission (as provided by the school)': "Please extract the Mission of the university.", 
        'Overview | General Information | Religious affiliation:': "Please extract the Religious affiliation of the university.", 
        'Overview | General Information | Setting:': "Please extract the Setting of the university.", 
        'Overview | General Information | Total undergraduate enrollment': "Please extract the Total undergraduate enrollment of the university.", 
        'Overview | General Information | Year founded:': "Please extract the Year founded of the university.", 
        'Rank': "Please extract the Rank of the university.", 
        'Score': "Please extract the Score of the university.", 
        'Tier': "Please extract the Tier of the university.", 
        'Web site:': "Please extract the Web site of the university.", 
        'topic_entity_name': "Please extract the topic_entity_name of the university."
        }
}