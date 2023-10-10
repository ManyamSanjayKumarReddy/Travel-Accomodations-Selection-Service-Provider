function searchRooms(rooms, searchTerm) {
    searchTerm = searchTerm.toLowerCase();
    return rooms.filter(function (room) {
        return (
            room.room_name.toLowerCase().includes(searchTerm) ||
            room.category.toLowerCase().includes(searchTerm) ||
            room.subcategory.toLowerCase().includes(searchTerm)
        );
    });
}
