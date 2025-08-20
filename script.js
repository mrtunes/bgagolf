// Course data structure: each course has 18 holes with par values
const courses = {
    "augusta_national": {
        "name": "Augusta National Golf Club",
        "location": "Augusta, GA",
        "par": [
            4,
            5,
            4,
            3,
            4,
            3,
            4,
            5,
            4,
            4,
            4,
            3,
            5,
            4,
            5,
            3,
            4,
            4
        ],
        "yardage": [
            445,
            575,
            350,
            170,
            495,
            180,
            450,
            570,
            460,
            495,
            505,
            155,
            510,
            440,
            530,
            170,
            440,
            465
        ]
    },
    "pebble_beach": {
        "name": "Pebble Beach Golf Links",
        "location": "Pebble Beach, CA",
        "par": [
            4,
            5,
            4,
            4,
            3,
            5,
            3,
            4,
            4,
            4,
            4,
            3,
            4,
            5,
            4,
            4,
            3,
            5
        ],
        "yardage": [
            381,
            502,
            388,
            327,
            188,
            516,
            106,
            431,
            466,
            446,
            380,
            202,
            404,
            580,
            397,
            403,
            178,
            543
        ]
    },
    "st_andrews": {
        "name": "The Old Course at St Andrews",
        "location": "St Andrews, Scotland",
        "par": [
            4,
            4,
            4,
            4,
            5,
            4,
            4,
            3,
            4,
            4,
            3,
            4,
            4,
            5,
            4,
            4,
            4,
            4
        ],
        "yardage": [
            376,
            453,
            397,
            480,
            568,
            412,
            372,
            166,
            352,
            386,
            174,
            348,
            465,
            614,
            456,
            423,
            461,
            357
        ]
    },
    "bethpage_black": {
        "name": "Bethpage State Park (Black Course)",
        "location": "Farmingdale, NY",
        "par": [
            4,
            4,
            3,
            5,
            4,
            4,
            4,
            3,
            4,
            4,
            4,
            4,
            5,
            3,
            4,
            4,
            4,
            4
        ],
        "yardage": [
            430,
            389,
            210,
            517,
            422,
            454,
            492,
            161,
            411,
            492,
            435,
            450,
            556,
            160,
            408,
            451,
            468,
            411
        ]
    },
    "torrey_pines": {
        "name": "Torrey Pines Golf Course (South)",
        "location": "La Jolla, CA",
        "par": [
            4,
            4,
            3,
            5,
            4,
            3,
            4,
            4,
            4,
            4,
            3,
            4,
            4,
            5,
            4,
            4,
            3,
            5
        ],
        "yardage": [
            454,
            387,
            198,
            609,
            452,
            177,
            456,
            437,
            492,
            408,
            221,
            504,
            417,
            570,
            422,
            422,
            230,
            570
        ]
    },
    "whistling_straits": {
        "name": "Whistling Straits (Straits Course)",
        "location": "Sheboygan, WI",
        "par": [
            4,
            4,
            3,
            5,
            4,
            3,
            5,
            4,
            4,
            4,
            3,
            4,
            4,
            5,
            4,
            4,
            3,
            4
        ],
        "yardage": [
            411,
            378,
            176,
            576,
            436,
            166,
            582,
            463,
            421,
            424,
            195,
            446,
            404,
            619,
            432,
            416,
            223,
            489
        ]
    },
    "pinehurst_no2": {
        "name": "Pinehurst No. 2",
        "location": "Pinehurst, NC",
        "par": [
            4,
            4,
            3,
            4,
            4,
            5,
            4,
            4,
            3,
            4,
            4,
            4,
            5,
            3,
            4,
            4,
            3,
            4
        ],
        "yardage": [
            404,
            446,
            163,
            529,
            482,
            574,
            407,
            485,
            164,
            611,
            434,
            441,
            608,
            194,
            360,
            508,
            187,
            446
        ]
    },
    "tpc_sawgrass": {
        "name": "TPC Sawgrass (Stadium Course)",
        "location": "Ponte Vedra Beach, FL",
        "par": [
            4,
            5,
            3,
            4,
            4,
            4,
            4,
            3,
            4,
            4,
            5,
            4,
            3,
            4,
            4,
            5,
            3,
            4
        ],
        "yardage": [
            423,
            532,
            177,
            384,
            466,
            393,
            442,
            219,
            583,
            424,
            558,
            358,
            181,
            481,
            449,
            535,
            137,
            447
        ]
    },
    "kiawah_ocean": {
        "name": "Kiawah Island Golf Resort (Ocean Course)",
        "location": "Kiawah Island, SC",
        "par": [
            4,
            4,
            4,
            4,
            3,
            5,
            4,
            3,
            4,
            4,
            5,
            3,
            4,
            4,
            4,
            5,
            3,
            4
        ],
        "yardage": [
            395,
            543,
            390,
            453,
            207,
            455,
            527,
            197,
            464,
            439,
            650,
            154,
            404,
            478,
            421,
            579,
            221,
            439
        ]
    },
    "oakmont": {
        "name": "Oakmont Country Club",
        "location": "Oakmont, PA",
        "par": [
            4,
            4,
            4,
            5,
            4,
            3,
            4,
            3,
            4,
            4,
            4,
            5,
            3,
            4,
            4,
            4,
            4,
            4
        ],
        "yardage": [
            482,
            341,
            428,
            609,
            382,
            194,
            479,
            228,
            478,
            435,
            379,
            667,
            185,
            358,
            453,
            231,
            313,
            484
        ]
    },
    "congressional": {
        "name": "Congressional Country Club (Blue Course)",
        "location": "Bethesda, MD",
        "par": [
            4,
            5,
            4,
            3,
            4,
            4,
            4,
            3,
            4,
            4,
            4,
            3,
            4,
            5,
            4,
            4,
            4,
            4
        ],
        "yardage": [
            421,
            581,
            456,
            201,
            418,
            480,
            445,
            195,
            465,
            508,
            417,
            204,
            440,
            555,
            479,
            477,
            440,
            468
        ]
    },
    "chambers_bay": {
        "name": "Chambers Bay Golf Course",
        "location": "University Place, WA",
        "par": [
            4,
            4,
            4,
            4,
            3,
            5,
            3,
            4,
            4,
            4,
            4,
            3,
            4,
            5,
            4,
            4,
            3,
            5
        ],
        "yardage": [
            418,
            440,
            492,
            491,
            194,
            516,
            179,
            420,
            524,
            401,
            336,
            155,
            434,
            632,
            402,
            375,
            134,
            641
        ]
    },
    "oakdale_1_3": {
        "name": "Oakdale Golf & Country Club (Course 1 & 3)",
        "location": "Toronto, ON, Canada",
        "par": [
            4,
            3,
            4,
            4,
            3,
            4,
            4,
            5,
            5,
            4,
            3,
            5,
            4,
            3,
            4,
            4,
            4,
            5
        ],
        "yardage": [
            379,
            188,
            361,
            374,
            223,
            330,
            381,
            492,
            470,
            281,
            207,
            553,
            400,
            186,
            418,
            398,
            432,
            479
        ]
    },
    "oakdale_1_2": {
        "name": "Oakdale Golf & Country Club (Course 1 & 2)",
        "location": "Toronto, ON, Canada",
        "par": [
            4,
            3,
            4,
            4,
            3,
            4,
            4,
            5,
            5,
            4,
            5,
            3,
            5,
            3,
            5,
            4,
            4,
            3
        ],
        "yardage": [
            379,
            188,
            361,
            374,
            223,
            330,
            381,
            492,
            470,
            432,
            545,
            148,
            590,
            213,
            560,
            432,
            354,
            191
        ]
    },
    "humber_valley_golf_club": {
        "name": "Humber Valley Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [
            4,
            4,
            4,
            3,
            4,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            3,
            5,
            5,
            3
        ],
        "yardage": [
            348,
            364,
            249,
            127,
            311,
            89,
            316,
            306,
            325,
            339,
            314,
            296,
            301,
            366,
            167,
            515,
            516,
            197
        ],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/humbervalleygc/detailedscorecard.htm"
    },
    "tpc_toronto_osprey_valley_north": {
        "name": "TPC Toronto at Osprey Valley - North",
        "location": "Toronto, ON, Canada",
        "par": [
            5,
            4,
            4,
            3,
            4,
            4,
            3,
            5,
            4,
            4,
            3,
            4,
            5,
            3,
            4,
            4,
            4,
            5
        ],
        "yardage": [
            496,
            428,
            376,
            140,
            402,
            312,
            170,
            494,
            388,
            370,
            149,
            328,
            514,
            144,
            338,
            420,
            416,
            494
        ],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/ospreyvalleytoot/detailedscorecard.htm"
    },
    "scarlett_woods_golf_club": {
        "name": "Scarlett Woods Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [
            4,
            3,
            3,
            3,
            3,
            3,
            4,
            3,
            3,
            3,
            4,
            4,
            3,
            4,
            4,
            3,
            3,
            4
        ],
        "yardage": [
            309,
            167,
            230,
            127,
            107,
            155,
            353,
            161,
            182,
            111,
            262,
            320,
            118,
            348,
            255,
            81,
            155,
            308
        ],
        "tee_info": "White Tees",
        "source": "golfcanada.ca",
        "url": "https://www.golfcanada.ca/golf-facility/scarlett-woods-golf-club-en/",
        "course_type": "Executive Course",
        "note": "Par 61 executive course with mix of par 3s and par 4s"
    },
    "don_valley_golf_club": {
        "name": "Don Valley Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [
            4,
            4,
            5,
            4,
            3,
            5,
            3,
            5,
            4,
            4,
            4,
            5,
            3,
            4,
            3,
            4,
            4,
            4
        ],
        "yardage": [
            329,
            464,
            502,
            429,
            177,
            540,
            164,
            525,
            292,
            320,
            345,
            490,
            152,
            375,
            138,
            305,
            291,
            325
        ],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/donvalleygc/detailedscorecard.htm"
    },
    "lebovic_golf_club": {
        "name": "Lebovic Golf Club",
        "location": "Aurora, ON, Canada",
        "par": [
            5,
            4,
            5,
            4,
            3,
            4,
            4,
            4,
            3,
            5,
            4,
            4,
            3,
            4,
            3,
            4,
            3,
            4
        ],
        "yardage": [
            523,
            416,
            546,
            322,
            131,
            385,
            373,
            330,
            180,
            563,
            408,
            397,
            181,
            453,
            170,
            409,
            185,
            442
        ],
        "tee_info": "Black Tees",
        "source": "18birdies.com and course research",
        "url": "https://18birdies.com/golf-courses/club/d0d21190-af72-11e7-9f6b-0680a328ea36/lebovic-golf-club",
        "course_type": "Championship Course",
        "designer": "Doug Carrick",
        "opened": "2015",
        "note": "Par 70 championship course built on Oak Ridges Moraine",
        "features": "Unique tunnel connects holes on each side of Leslie Street"
    },
    "station_creek_golf_club_north": {
        "name": "Station Creek Golf Club - North",
        "location": "Stouffville, ON, Canada",
        "par": [
            4,
            3,
            4,
            4,
            3,
            4,
            4,
            3,
            5,
            5,
            4,
            3,
            5,
            4,
            4,
            4,
            3,
            4
        ],
        "yardage": [
            465,
            176,
            384,
            360,
            168,
            377,
            407,
            142,
            505,
            515,
            451,
            150,
            586,
            402,
            311,
            419,
            176,
            401
        ],
        "tee_info": "Blue Tees",
        "source": "golfify.io",
        "url": "https://www.golfify.io/courses/station-creek-golf-club-north",
        "course_type": "Championship Course"
    },
    "station_creek_golf_club_south": {
        "name": "Station Creek Golf Club - South",
        "location": "Stouffville, ON, Canada",
        "par": [
            4,
            4,
            5,
            3,
            4,
            4,
            4,
            3,
            5,
            5,
            3,
            4,
            4,
            4,
            3,
            4,
            5,
            4
        ],
        "yardage": [
            399,
            393,
            500,
            171,
            365,
            399,
            431,
            197,
            575,
            498,
            215,
            437,
            435,
            405,
            187,
            340,
            512,
            436
        ],
        "tee_info": "Blue Tees",
        "source": "golfify.io",
        "url": "https://www.golfify.io/courses/station-creek-golf-club-south",
        "course_type": "Championship Course"
    }
};;;;;;;;;;;

// Calculate BGA scores (par + 1)
function calculateBogeyScores(parArray) {
    return parArray.map(par => par + 1);
}

// Calculate totals for front 9, back 9, and total
function calculateTotals(scoreArray) {
    const front9 = scoreArray.slice(0, 9).reduce((sum, score) => sum + score, 0);
    const back9 = scoreArray.slice(9).reduce((sum, score) => sum + score, 0);
    const total = front9 + back9;
    return { front9, back9, total };
}

// Render modern card-based scorecard
function renderScorecard(courseKey) {
    const course = courses[courseKey];
    const bgaScores = calculateBogeyScores(course.par);
    const parTotals = calculateTotals(course.par);
    const bgaTotals = calculateTotals(bgaScores);
    
    // Clear existing content
    document.getElementById('frontNineHoles').innerHTML = '';
    document.getElementById('backNineHoles').innerHTML = '';
    
    // Update course info
    document.getElementById('courseName').textContent = course.name;
    document.getElementById('courseDetails').textContent = `${course.location} • Par ${parTotals.total} • BGA ${bgaTotals.total}`;
    document.getElementById('bgaTotal').textContent = bgaTotals.total;
    
    // Show/hide nine sections based on game format
    const frontNineSection = document.querySelector('.front-nine');
    const backNineSection = document.querySelector('.back-nine');
    
    if (gameFormat === 'back9') {
        frontNineSection.style.display = 'none';
        backNineSection.style.display = 'block';
    } else if (gameFormat === 'front9') {
        frontNineSection.style.display = 'block';
        backNineSection.style.display = 'none';
    } else {
        frontNineSection.style.display = 'block';
        backNineSection.style.display = 'block';
    }
    
    // Create hole cards for front nine (holes 1-9)
    const frontNineContainer = document.getElementById('frontNineHoles');
    if (gameFormat !== 'back9') {
        for (let i = 0; i < 9; i++) {
            const holeCard = createHoleCard(i + 1, course.par[i], bgaScores[i], course.yardage[i]);
            frontNineContainer.appendChild(holeCard);
        }
    }
    
    // Create hole cards for back nine (holes 10-18)
    const backNineContainer = document.getElementById('backNineHoles');
    if (gameFormat !== 'front9') {
        for (let i = 9; i < 18; i++) {
            const holeCard = createHoleCard(i + 1, course.par[i], bgaScores[i], course.yardage[i]);
            backNineContainer.appendChild(holeCard);
        }
    }
    
    // Initialize score tracking
    currentCourse = courseKey;
    
    // Save current course selection
    localStorage.setItem('bgaCurrentCourse', courseKey);
    
    // Load saved scores for this course
    setTimeout(() => {
        loadScores();
        updateScoreSummary();
    }, 100);
    
    document.getElementById('courseDisplay').style.display = 'block';
}

// Create a hole card element
function createHoleCard(holeNumber, par, bgaPar, yardage) {
    const card = document.createElement('div');
    card.className = 'hole-card';
    card.id = `hole-${holeNumber}`;
    
    card.innerHTML = `
        <div class="performance-indicator" id="indicator-${holeNumber}"></div>
        <div class="hole-header">
            <div class="hole-number">Hole ${holeNumber}</div>
            <div class="hole-yardage">${yardage} yds</div>
        </div>
        <div class="bga-par">
            <div class="bga-par-label">BGA Par</div>
            <div class="bga-par-value">${bgaPar}</div>
        </div>
        <div class="score-input-container">
            <input type="number" 
                   class="score-input" 
                   id="score-${holeNumber}"
                   min="1" 
                   max="12" 
                   placeholder="?"
                   onchange="updateHoleScore(${holeNumber}, ${bgaPar})"
                   onkeyup="updateHoleScore(${holeNumber}, ${bgaPar})">
        </div>
    `;
    
    return card;
}

// Update hole score and visual feedback
function updateHoleScore(holeNumber, bgaPar) {
    const input = document.getElementById(`score-${holeNumber}`);
    const card = document.getElementById(`hole-${holeNumber}`);
    const indicator = document.getElementById(`indicator-${holeNumber}`);
    const score = parseInt(input.value);
    
    // Clear existing classes
    card.classList.remove('under-bga', 'at-bga', 'over-bga');
    input.classList.remove('under', 'at', 'over');
    indicator.classList.remove('under', 'at', 'over');
    
    if (score && score > 0) {
        if (score < bgaPar) {
            card.classList.add('under-bga');
            input.classList.add('under');
            indicator.classList.add('under');
        } else if (score === bgaPar) {
            card.classList.add('at-bga');
            input.classList.add('at');
            indicator.classList.add('at');
        } else {
            card.classList.add('over-bga');
            input.classList.add('over');
            indicator.classList.add('over');
        }
    }
    
    // Save score to localStorage
    saveScore(holeNumber, score);
    
    updateScoreSummary();
}

// Update score summary
let currentCourse = null;
let gameFormat = 'full18'; // 'full18', 'front9', 'back9'

function updateScoreSummary() {
    if (!currentCourse) return;
    
    const course = courses[currentCourse];
    const bgaScores = calculateBogeyScores(course.par);
    
    let totalScore = 0;
    let holesPlayed = 0;
    let totalBGA = 0;
    let expectedHoles = 18;
    
    // Determine which holes to count based on game format
    let startHole = 1;
    let endHole = 18;
    
    if (gameFormat === 'front9') {
        startHole = 1;
        endHole = 9;
        expectedHoles = 9;
    } else if (gameFormat === 'back9') {
        startHole = 10;
        endHole = 18;
        expectedHoles = 9;
    }
    
    for (let i = startHole; i <= endHole; i++) {
        const input = document.getElementById(`score-${i}`);
        if (input) {
            const score = parseInt(input.value);
            if (score && score > 0) {
                totalScore += score;
                holesPlayed++;
            }
        }
        totalBGA += bgaScores[i - 1];
    }
    
    document.getElementById('totalScore').textContent = holesPlayed > 0 ? totalScore : '-';
    document.getElementById('holesPlayed').textContent = `${holesPlayed}/${expectedHoles}`;
    document.getElementById('bgaTotal').textContent = totalBGA;
    
    if (holesPlayed === expectedHoles) {
        const vsBGA = totalScore - totalBGA;
        const vsBGADisplay = vsBGA > 0 ? `+${vsBGA}` : vsBGA.toString();
        document.getElementById('vseBGA').textContent = vsBGADisplay;
    } else if (holesPlayed > 0) {
        // Show partial comparison for played holes only
        let playedBGA = 0;
        for (let i = startHole; i <= endHole; i++) {
            const input = document.getElementById(`score-${i}`);
            if (input && parseInt(input.value) > 0) {
                playedBGA += bgaScores[i - 1];
            }
        }
        const vsBGA = totalScore - playedBGA;
        const vsBGADisplay = vsBGA > 0 ? `+${vsBGA}` : vsBGA.toString();
        document.getElementById('vseBGA').textContent = vsBGADisplay;
    } else {
        document.getElementById('vseBGA').textContent = '-';
    }
}

// Save score to localStorage
function saveScore(holeNumber, score) {
    if (!currentCourse) return;
    
    const savedScores = JSON.parse(localStorage.getItem('bgaScores') || '{}');
    if (!savedScores[currentCourse]) {
        savedScores[currentCourse] = {};
    }
    
    if (score && score > 0) {
        savedScores[currentCourse][holeNumber] = score;
    } else {
        delete savedScores[currentCourse][holeNumber];
    }
    
    localStorage.setItem('bgaScores', JSON.stringify(savedScores));
}

// Load scores from localStorage
function loadScores() {
    if (!currentCourse) return;
    
    const savedScores = JSON.parse(localStorage.getItem('bgaScores') || '{}');
    const courseScores = savedScores[currentCourse] || {};
    const course = courses[currentCourse];
    const bgaScores = calculateBogeyScores(course.par);
    
    for (let i = 1; i <= 18; i++) {
        const input = document.getElementById(`score-${i}`);
        if (input && courseScores[i]) {
            input.value = courseScores[i];
            
            // Apply visual updates without triggering save
            const card = document.getElementById(`hole-${i}`);
            const indicator = document.getElementById(`indicator-${i}`);
            const score = courseScores[i];
            const bgaPar = bgaScores[i - 1];
            
            // Clear existing classes
            card.classList.remove('under-bga', 'at-bga', 'over-bga');
            input.classList.remove('under', 'at', 'over');
            indicator.classList.remove('under', 'at', 'over');
            
            if (score < bgaPar) {
                card.classList.add('under-bga');
                input.classList.add('under');
                indicator.classList.add('under');
            } else if (score === bgaPar) {
                card.classList.add('at-bga');
                input.classList.add('at');
                indicator.classList.add('at');
            } else {
                card.classList.add('over-bga');
                input.classList.add('over');
                indicator.classList.add('over');
            }
        }
    }
}

// Clear all scores
function clearAllScores() {
    for (let i = 1; i <= 18; i++) {
        const input = document.getElementById(`score-${i}`);
        const card = document.getElementById(`hole-${i}`);
        const indicator = document.getElementById(`indicator-${i}`);
        
        if (input) {
            input.value = '';
            input.classList.remove('under', 'at', 'over');
        }
        if (card) {
            card.classList.remove('under-bga', 'at-bga', 'over-bga');
        }
        if (indicator) {
            indicator.classList.remove('under', 'at', 'over');
        }
    }
    
    // Clear from localStorage
    if (currentCourse) {
        const savedScores = JSON.parse(localStorage.getItem('bgaScores') || '{}');
        delete savedScores[currentCourse];
        localStorage.setItem('bgaScores', JSON.stringify(savedScores));
    }
    
    // Reset holes played counter
    document.getElementById('holesPlayed').textContent = '0/18';
    updateScoreSummary();
}

// Initialize the page
function init() {
    const countrySelect = document.getElementById('countrySelect');
    const courseSelect = document.getElementById('courseSelect');
    
    // Populate country dropdown
    populateCountryDropdown();
    
    // Populate course dropdown (initially all courses)
    populateCourseDropdown();
    
    // Handle country filter
    countrySelect.addEventListener('change', function() {
        filterCoursesByCountry(this.value);
    });
    
    // Handle course selection
    courseSelect.addEventListener('change', function() {
        if (this.value) {
            // Show game format selector instead of immediately showing scorecard
            document.getElementById('gameFormatSelector').style.display = 'block';
            document.getElementById('courseDisplay').style.display = 'none';
            currentCourse = this.value;
        } else {
            document.getElementById('gameFormatSelector').style.display = 'none';
            document.getElementById('courseDisplay').style.display = 'none';
        }
    });
    
    // Handle start round button
    document.getElementById('startRound').addEventListener('click', function() {
        if (currentCourse) {
            gameFormat = document.getElementById('gameFormat').value;
            renderScorecard(currentCourse);
        }
    });
    
    // Restore last selected course on page load
    const lastCourse = localStorage.getItem('bgaCurrentCourse');
    if (lastCourse && courses[lastCourse]) {
        courseSelect.value = lastCourse;
        renderScorecard(lastCourse);
    }
}

// Extract country from location string
function extractCountry(location) {
    // Handle different location formats
    const parts = location.split(',').map(part => part.trim());
    
    // If last part looks like a country (common patterns)
    const lastPart = parts[parts.length - 1];
    
    // Common country patterns
    if (lastPart === 'Canada' || lastPart.includes('ON') || lastPart.includes('Canada')) {
        return 'Canada';
    } else if (lastPart === 'USA' || lastPart.length === 2 || 
               ['CA', 'FL', 'TX', 'NY', 'PA', 'NC', 'SC', 'GA', 'MD', 'WA', 'WI'].includes(lastPart)) {
        return 'United States';
    } else if (lastPart === 'Scotland' || lastPart === 'England' || lastPart === 'UK') {
        return 'United Kingdom';
    } else if (lastPart.length > 2) {
        return lastPart;
    }
    
    // Default to USA for state abbreviations or unknown
    return 'United States';
}

// Populate country dropdown
function populateCountryDropdown() {
    const countrySelect = document.getElementById('countrySelect');
    const countries = new Set();
    
    // Extract unique countries from all courses
    Object.values(courses).forEach(course => {
        const country = extractCountry(course.location);
        countries.add(country);
    });
    
    // Sort countries alphabetically
    const sortedCountries = Array.from(countries).sort();
    
    // Add countries to dropdown
    sortedCountries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countrySelect.appendChild(option);
    });
}

// Populate course dropdown
function populateCourseDropdown(filteredCourses = null) {
    const courseSelect = document.getElementById('courseSelect');
    
    // Clear existing options except the first one
    while (courseSelect.children.length > 1) {
        courseSelect.removeChild(courseSelect.lastChild);
    }
    
    // Reset first option
    courseSelect.children[0].textContent = 'Choose a course...';
    courseSelect.value = '';
    
    // Use filtered courses or all courses
    const coursesToShow = filteredCourses || courses;
    
    // Create array of courses with country info for sorting
    const courseArray = Object.keys(coursesToShow).map(courseKey => ({
        key: courseKey,
        course: coursesToShow[courseKey],
        country: extractCountry(coursesToShow[courseKey].location)
    }));
    
    // Sort alphabetically by course name
    courseArray.sort((a, b) => a.course.name.localeCompare(b.course.name));
    
    // Add courses to dropdown
    courseArray.forEach(({key, course}) => {
        const option = document.createElement('option');
        option.value = key;
        option.textContent = course.name + (course.userAdded ? ' (Added by You)' : '');
        courseSelect.appendChild(option);
    });
    
    // Update course count
    const courseCount = courseArray.length;
    if (courseCount === 0) {
        courseSelect.children[0].textContent = 'No courses found';
    } else {
        courseSelect.children[0].textContent = `Choose from ${courseCount} course${courseCount === 1 ? '' : 's'}...`;
    }
}

// Filter courses by country
function filterCoursesByCountry(selectedCountry) {
    const courseSelect = document.getElementById('courseSelect');
    
    // Hide current course display
    document.getElementById('courseDisplay').style.display = 'none';
    
    if (!selectedCountry) {
        // Show all courses
        populateCourseDropdown();
        return;
    }
    
    // Filter courses by selected country
    const filteredCourses = {};
    Object.keys(courses).forEach(courseKey => {
        const course = courses[courseKey];
        const courseCountry = extractCountry(course.location);
        
        if (courseCountry === selectedCountry) {
            filteredCourses[courseKey] = course;
        }
    });
    
    // Update course dropdown with filtered courses
    populateCourseDropdown(filteredCourses);
}

// Image upload and OCR functionality
let userCourses = JSON.parse(localStorage.getItem('userCourses')) || {};

function initImageUpload() {
    const addCourseBtn = document.getElementById('addCourseBtn');
    const modal = document.getElementById('addCourseModal');
    const cancelBtn = document.getElementById('cancelAdd');
    const photoInput = document.getElementById('scorecardPhoto');
    const imagePreview = document.getElementById('imagePreview');
    const ocrProgress = document.getElementById('ocrProgress');
    const courseForm = document.getElementById('courseForm');
    const saveCourseBtn = document.getElementById('saveCourse');
    
    // Open modal
    addCourseBtn.addEventListener('click', () => {
        modal.style.display = 'block';
        resetForm();
    });
    
    // Close modal
    cancelBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });
    
    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
    
    // Handle file upload
    photoInput.addEventListener('change', handleImageUpload);
    
    // Save course
    saveCourseBtn.addEventListener('click', saveCourse);
    
    // Generate hole inputs
    generateHoleInputs();
}

function resetForm() {
    document.getElementById('scorecardPhoto').value = '';
    document.getElementById('imagePreview').innerHTML = '';
    document.getElementById('ocrProgress').style.display = 'none';
    document.getElementById('courseForm').style.display = 'none';
    document.getElementById('courseName').value = '';
    document.getElementById('courseLocation').value = '';
    
    // Reset hole inputs
    for (let i = 1; i <= 18; i++) {
        document.getElementById(`par${i}`).value = '';
        document.getElementById(`yardage${i}`).value = '';
    }
}

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    // Show image preview
    const reader = new FileReader();
    reader.onload = function(e) {
        const imagePreview = document.getElementById('imagePreview');
        imagePreview.innerHTML = `
            <img src="${e.target.result}" style="max-width: 100%; max-height: 200px; border-radius: 4px; border: 1px solid #ddd;">
        `;
        
        // Start OCR processing
        processImageWithOCR(e.target.result);
    };
    reader.readAsDataURL(file);
}

function processImageWithOCR(imageData) {
    const ocrProgress = document.getElementById('ocrProgress');
    const courseForm = document.getElementById('courseForm');
    
    ocrProgress.style.display = 'block';
    
    // Simulate OCR processing (in real implementation, this would use Tesseract.js or API)
    setTimeout(() => {
        // Mock OCR results
        const mockResults = {
            courseName: 'Sample Golf Course',
            location: 'Sample City, State',
            holes: [
                { hole: 1, par: 4, yardage: 380 },
                { hole: 2, par: 3, yardage: 165 },
                { hole: 3, par: 5, yardage: 520 },
                { hole: 4, par: 4, yardage: 410 },
                { hole: 5, par: 3, yardage: 180 },
                { hole: 6, par: 4, yardage: 350 },
                { hole: 7, par: 5, yardage: 580 },
                { hole: 8, par: 4, yardage: 420 },
                { hole: 9, par: 4, yardage: 390 },
                { hole: 10, par: 4, yardage: 400 },
                { hole: 11, par: 3, yardage: 170 },
                { hole: 12, par: 4, yardage: 360 },
                { hole: 13, par: 5, yardage: 550 },
                { hole: 14, par: 4, yardage: 430 },
                { hole: 15, par: 3, yardage: 190 },
                { hole: 16, par: 4, yardage: 380 },
                { hole: 17, par: 4, yardage: 370 },
                { hole: 18, par: 5, yardage: 540 }
            ]
        };
        
        populateFormWithOCRResults(mockResults);
        ocrProgress.style.display = 'none';
        courseForm.style.display = 'block';
    }, 3000);
}

function populateFormWithOCRResults(results) {
    document.getElementById('courseName').value = results.courseName;
    document.getElementById('courseLocation').value = results.location;
    
    results.holes.forEach(hole => {
        document.getElementById(`par${hole.hole}`).value = hole.par;
        document.getElementById(`yardage${hole.hole}`).value = hole.yardage;
    });
}

function generateHoleInputs() {
    const holeInputs = document.getElementById('holeInputs');
    let html = '';
    
    for (let i = 1; i <= 18; i++) {
        html += `
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 5px;">
                <div style="text-align: center; padding: 8px; background: #f9f9f9; border-radius: 4px;">${i}</div>
                <input type="number" id="par${i}" min="3" max="5" style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; text-align: center;">
                <input type="number" id="yardage${i}" min="50" max="800" style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; text-align: center;">
            </div>
        `;
    }
    
    holeInputs.innerHTML = html;
}

function saveCourse() {
    const courseName = document.getElementById('courseName').value.trim();
    const courseLocation = document.getElementById('courseLocation').value.trim();
    
    if (!courseName || !courseLocation) {
        alert('Please fill in course name and location');
        return;
    }
    
    // Collect hole data
    const parArray = [];
    const yardageArray = [];
    
    for (let i = 1; i <= 18; i++) {
        const par = parseInt(document.getElementById(`par${i}`).value);
        const yardage = parseInt(document.getElementById(`yardage${i}`).value);
        
        if (!par || par < 3 || par > 5) {
            alert(`Please enter valid par for hole ${i} (3-5)`);
            return;
        }
        
        if (!yardage || yardage < 50 || yardage > 800) {
            alert(`Please enter valid yardage for hole ${i} (50-800)`);
            return;
        }
        
        parArray.push(par);
        yardageArray.push(yardage);
    }
    
    // Create course object
    const courseKey = createSafeKey(courseName);
    const newCourse = {
        name: courseName,
        location: courseLocation,
        par: parArray,
        yardage: yardageArray,
        userAdded: true
    };
    
    // Save to user courses
    userCourses[courseKey] = newCourse;
    localStorage.setItem('userCourses', JSON.stringify(userCourses));
    
    // Add to main courses object
    courses[courseKey] = newCourse;
    
    // Update dropdown
    updateCourseDropdown();
    
    // Close modal and show success
    document.getElementById('addCourseModal').style.display = 'none';
    alert(`Successfully added ${courseName}!`);
    
    // Auto-select the new course
    document.getElementById('courseSelect').value = courseKey;
    renderScorecard(courseKey);
}

function createSafeKey(courseName) {
    let baseKey = courseName.toLowerCase().replace(/[^a-z0-9]/g, '_');
    let counter = 1;
    let safeKey = baseKey;
    
    // Ensure unique key
    while (courses[safeKey] || userCourses[safeKey]) {
        safeKey = `${baseKey}_${counter}`;
        counter++;
    }
    
    return safeKey;
}

function updateCourseDropdown() {
    // Update the global courses object with user courses
    Object.keys(userCourses).forEach(courseKey => {
        courses[courseKey] = userCourses[courseKey];
    });
    
    // Repopulate both country and course dropdowns
    populateCountryDropdown();
    populateCourseDropdown();
}

// Load user courses on startup
function loadUserCourses() {
    Object.keys(userCourses).forEach(courseKey => {
        courses[courseKey] = userCourses[courseKey];
    });
}

// CSV Export functionality
function exportScorecard() {
    if (!currentCourse) {
        alert('Please select a course first');
        return;
    }
    
    const course = courses[currentCourse];
    const bgaScores = calculateBogeyScores(course.par);
    const currentDate = new Date().toLocaleDateString();
    
    // Determine which holes to export based on game format
    let startHole = 1;
    let endHole = 18;
    let formatName = 'Full 18 Holes';
    
    if (gameFormat === 'front9') {
        startHole = 1;
        endHole = 9;
        formatName = 'Front 9';
    } else if (gameFormat === 'back9') {
        startHole = 10;
        endHole = 18;
        formatName = 'Back 9';
    }
    
    // Create CSV content
    let csvContent = '';
    
    // Header information
    csvContent += `BGA Golf Scorecard\n`;
    csvContent += `Course:,${course.name}\n`;
    csvContent += `Location:,${course.location}\n`;
    csvContent += `Date:,${currentDate}\n`;
    csvContent += `Format:,${formatName}\n`;
    csvContent += `\n`;
    
    // Column headers
    csvContent += `Hole,Par,BGA Par,Yardage,Your Score,vs BGA\n`;
    
    // Hole data
    let totalScore = 0;
    let totalBGA = 0;
    let holesWithScores = 0;
    
    for (let i = startHole; i <= endHole; i++) {
        const par = course.par[i - 1];
        const bgaPar = bgaScores[i - 1];
        const yardage = course.yardage[i - 1];
        const scoreInput = document.getElementById(`score-${i}`);
        const score = scoreInput ? parseInt(scoreInput.value) || '' : '';
        
        let vsBGA = '';
        if (score !== '') {
            const diff = score - bgaPar;
            vsBGA = diff > 0 ? `+${diff}` : diff.toString();
            totalScore += score;
            holesWithScores++;
        }
        
        totalBGA += bgaPar;
        
        csvContent += `${i},${par},${bgaPar},${yardage},${score},${vsBGA}\n`;
    }
    
    // Summary
    csvContent += `\n`;
    csvContent += `Summary\n`;
    csvContent += `Holes Played:,${holesWithScores}\n`;
    csvContent += `Total Score:,${totalScore || '-'}\n`;
    csvContent += `Total BGA:,${totalBGA}\n`;
    if (totalScore > 0) {
        const totalVsBGA = totalScore - totalBGA;
        csvContent += `vs BGA:,${totalVsBGA > 0 ? '+' + totalVsBGA : totalVsBGA}\n`;
    }
    
    // Download the CSV file
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    
    // Generate filename
    const courseName = course.name.replace(/[^a-z0-9]/gi, '_').toLowerCase();
    const filename = `BGA_${courseName}_${formatName.replace(' ', '_')}_${currentDate.replace(/\//g, '-')}.csv`;
    link.setAttribute('download', filename);
    
    // Trigger download
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Start the application
document.addEventListener('DOMContentLoaded', () => {
    loadUserCourses();
    init();
    initImageUpload();
    
    // Add CSV export button event listener
    document.getElementById('exportCsvBtn').addEventListener('click', exportScorecard);
});