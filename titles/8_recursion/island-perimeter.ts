function islandPerimeter(grid: number[][]): number {
    let n= grid.length
    let m= grid[0].length
    let seen = new Set<string>();
    let directions =new Map([[-1, 0], [0, -1], [1, 0], [0, 1]])
    function in_bound(row:number, col:number):boolean{
        return 0<=row && row <n && 0 <= col&& col < m 
    }
    function stringFy(row:number, col:number):string{
        const st:state={row, col}
        return JSON.stringify(st)
    }
    function dfs(row, col){
        let side, count=0
        for (const [dr, dc] of directions){
            let nrow= row + dr
            let ncol = col + dc
            if (!in_bound(nrow, ncol) || grid[nrow][ncol]==0){
                side++
                continue
            }            
            let new_state=stringFy(nrow, ncol)
            if(!seen.has(new_state)){
                seen.add(new_state)
                count+=dfs(nrow, ncol)
            }            
        }
        return side + count
    }
    for (let r = 0; r < n; r++) {
        for(let c=0; c<m; c++){
            if (grid[r][c]===1 && !seen.has(stringFy(r,c))){
                seen.add(stringFy(r,c))
                return dfs(r,c)
            }
        }
    }
    
    return 0
};
interface state{
    row:number
    col:number
}