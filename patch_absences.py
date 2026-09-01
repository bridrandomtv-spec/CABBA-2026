import sys

with open('src/components/MatchCenter.tsx', 'r') as f:
    content = f.read()

# Add import
if 'MatchAbsences' not in content:
    content = content.replace("import MatchCalendar from './MatchCalendar';", "import MatchCalendar from './MatchCalendar';\nimport MatchAbsences from './MatchAbsences';")

old_formation_end = """              {/* Goalkeeper */}
              <div className="flex justify-center mt-2">
                <PlayerNode number="1" name="حارس" />
              </div>
            </div>
          </div>
        </div>
      )}"""

new_formation_end = """              {/* Goalkeeper */}
              <div className="flex justify-center mt-2">
                <PlayerNode number="1" name="حارس" />
              </div>
            </div>
          </div>
          <MatchAbsences />
        </div>
      )}"""

if old_formation_end in content:
    content = content.replace(old_formation_end, new_formation_end)
else:
    print("Failed to match block")

with open('src/components/MatchCenter.tsx', 'w') as f:
    f.write(content)
