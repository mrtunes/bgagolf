# Bogey Golf - BGA Scorecards

A web application for golf enthusiasts that displays interactive scorecards with BGA (Bogey Golf) scoring, where par+1 is displayed for every hole. The app features course data from around the world with automated scraping capabilities.

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
   git clone https://github.com/mrtunes/bgagolf.git
   cd bgagolf
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

All course data lives in the `courses` object at the top of `script.js`. To add a new course:

### 1. Find the scorecard

Search for the course scorecard online. Good sources:
- **GolfPass** (golfpass.com) — most reliable for hole-by-hole data
- **BlueGolf** (course.bluegolf.com) — detailed scorecards, but may block automated fetching
- **Course website** — often has a PDF scorecard

You need 18 par values and 18 yardage values for a single tee set (typically the championship tees).

### 2. Add the entry to `script.js`

Add a new entry to the `courses` object at the bottom of the list, before the closing `}`. Follow this format:

```javascript
"course_key": {
    "name": "Course Name",
    "location": "City, Province/State, Country",
    "par": [4, 3, 5, ...],       // 18 values
    "yardage": [420, 180, 530, ...], // 18 values
    "tee_info": "Gold Tees",
    "source": "golfpass.com",
    "url": "https://source-url",
    "course_type": "Championship Course"
}
```

### 3. Verify the data

- Par array has exactly 18 values (each 3, 4, or 5)
- Yardage array has exactly 18 values
- Total par matches the course (usually 70-72)
- Total yardage is reasonable (5,500-7,500)

## File Structure

```
bgagolf/
├── index.html              # Main application
├── script.js               # JavaScript logic and ALL course data
├── all_courses.json        # Legacy JSON export (not used by the app)
├── scorecard-scrapes/      # Saved HTML pages from course websites
├── scraper.py              # Golf Course API scraper (legacy)
├── bluegolf_scraper_v2.py  # BlueGolf.com scraper (legacy)
├── add_*.py                # One-off course addition scripts (legacy)
└── requirements.txt        # Python dependencies (for legacy scrapers)
```

## Course Data Sources

- **GolfPass** (golfpass.com) — hole-by-hole scorecards, most reliable
- **BlueGolf** (course.bluegolf.com) — detailed scorecards for many courses
- **Course websites** — official PDF scorecards
- **Manual research** — verified from official sources

## BGA Scoring System

The BGA scoring system displays par+1 for each hole:
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