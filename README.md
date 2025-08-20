# BGA Claude - Bogey Golf Association

A web application for golf enthusiasts that displays interactive scorecards with BGA (Bogey Golf Association) scoring, where par+1 is displayed for every hole. The app features course data from around the world with automated scraping capabilities.

## Features

- **BGA Scoring System**: Shows par+1 for each hole instead of traditional par
- **Interactive Scorecards**: Card-based layout with real-time score tracking
- **Country Filtering**: Sort courses by country before selection
- **Performance Indicators**: Color-coded scoring relative to BGA par
- **Course Data**: 19+ golf courses from USA, Canada, and Scotland
- **Responsive Design**: Mobile-friendly interface
- **User Score Tracking**: Input and track your scores against BGA par

## Course Collection

The app includes championship courses from:
- **USA**: Augusta National, Pebble Beach, Bethpage Black, TPC Sawgrass, and more
- **Canada**: Toronto area courses including Oakdale, Humber Valley, Don Valley, Lebovic Golf Club
- **Scotland**: The Old Course at St Andrews

## Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Storage**: JSON files with course information
- **Scraping**: Python with BeautifulSoup4 for automated course data collection
- **APIs**: Golf Course API integration, BlueGolf.com scraping

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/BGAClaude.git
   cd BGAClaude
   ```

2. **Open the application**
   - Simply open `index.html` in your web browser
   - No server setup required - runs entirely in the browser

3. **Using the app**
   - Select a country from the dropdown
   - Choose a golf course
   - Enter your scores for each hole
   - View your performance against BGA par

## Course Data Structure

Each course contains:
- Course name and location
- 18-hole par values
- Yardage information
- Tee information (Blue, White, etc.)
- Source attribution

## Adding New Courses

### Automated Scraping
The project includes Python scrapers for:
- Golf Course API
- BlueGolf.com courses
- Manual data extraction tools

### Running Scrapers
```bash
# Install dependencies
pip install -r requirements.txt

# Run specific scrapers
python scraper.py
python bluegolf_scraper_v2.py
```

### Manual Course Addition
Use the provided scripts to add courses manually:
- `add_oakdale.py` - Example course addition
- `add_humber_valley.py` - BlueGolf course addition
- `manual_courses.py` - General manual addition

## File Structure

```
BGAClaude/
├── index.html              # Main application
├── script.js               # JavaScript logic and course data
├── all_courses.json        # JSON course database
├── scraper.py             # Golf Course API scraper
├── bluegolf_scraper_v2.py # BlueGolf.com scraper
├── requirements.txt       # Python dependencies
├── add_*.py              # Course addition scripts
└── scorecard-scrapes/    # Saved HTML pages
```

## Course Data Sources

- **Golf Course API**: Professional course data
- **BlueGolf.com**: Detailed scorecards for Canadian courses
- **Manual Research**: Verified course information from official sources

## BGA Scoring System

The Bogey Golf Association scoring system displays par+1 for each hole:
- Par 3 → BGA 4
- Par 4 → BGA 5  
- Par 5 → BGA 6

This creates a more achievable scoring system for amateur golfers while maintaining the challenge and strategy of the game.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add new courses or improve functionality
4. Submit a pull request

## Future Enhancements

- [ ] User authentication and score persistence
- [ ] Course difficulty ratings
- [ ] Statistical analysis and handicap tracking
- [ ] Mobile app version
- [ ] Social features and leaderboards

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions about course data or features, please open an issue on GitHub.